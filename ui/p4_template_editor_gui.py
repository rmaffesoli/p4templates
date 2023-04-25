import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QDialog,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QListWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
)

from p4_templates.kernel.utils import read_json, convert_to_string

class P4TemplateEditorDialog(QDialog):
    def __init__(self, parent=None, template_path=None):
        super(P4TemplateEditorDialog, self).__init__(parent)
        self.template_path = template_path

        self.defaults = {
            "depot": {
                "name": "None",
                "type": "stream",
                "depth": "1",
                "user": "None",
            },
            "group": {
                "name": "None",
                "description": "",
                "max_results": "unset",
                "max_scan_rows": "unset",
                "max_lock_time": "unset",
                "max_open_files": "unset",
                "timeout": "43200",
                "password_timeout": "unset",
                "subgroups": "",
                "owners": "",
                "users": "",
            },
            "user": {
                "name": "",
                "email": "",
                "full_name": "",
                "auth_method": "",
                "reviews": "",
                "job_view": "",
            },
            "stream": {
                "name": "",
                "type": "mainline",
                "depot": "",
                "user": os.getenv("P4USER"),
                "view": "inherit",
                "parent": "",
                "options": "allsubmit unlocked notoparent nofromparent mergedown",
            },
            "protection": {
                "access": "",
                "type": "",
                "name": "",
                "host": "*",
                "path": "",
                "comment": "",
            },
            "branch": {"name": "", "owner": "", "options": "unlocked"},
        }

        self.create_ui_elements()        
        self.add_ui_elements_to_layout()
        self.set_window_settings()

        self.populate_data()
        self.exec()

    def create_ui_elements(self):
        self.btn_reload = QPushButton("Reload")
        self.btn_save = QPushButton("Save")

        self.main_tab_widget = QTabWidget()

        self.depot_tab = QWidget()

        self.depot_list = QListWidget()
        self.add_depot_btn = QPushButton("+")
        self.remove_depot_btn = QPushButton("-")
        self.depot_table = QTableWidget()

        self.depot_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.depot_table.horizontalHeader().setVisible(False)
        self.depot_table.verticalHeader().setVisible(False)
        self.depot_table.setColumnCount(2)
        self.depot_table.setRowCount(4)

        self.stream_tab = QWidget()
        self.stream_list = QListWidget()
        self.add_stream_btn = QPushButton("+")
        self.remove_stream_btn = QPushButton("-")
        self.stream_table = QTableWidget()

        self.stream_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.stream_table.horizontalHeader().setVisible(False)
        self.stream_table.verticalHeader().setVisible(False)
        self.stream_table.setColumnCount(2)
        self.stream_table.setRowCount(7)

        self.stream_view_tab_widget = QTabWidget()
        
        self.stream_paths_tab = QWidget()
        self.stream_paths_list = QListWidget()
        self.add_stream_paths_btn = QPushButton("+")
        self.remove_stream_paths_btn = QPushButton("-")

        self.stream_remapped_tab = QWidget()
        self.stream_remapped_table = QTableWidget()
        self.add_streams_remapped_btn = QPushButton("+")
        self.remove_streams_remapped_btn = QPushButton("-")

        self.stream_ignored_tab = QWidget()
        self.stream_ignored_list = QListWidget()
        self.add_streams_ignored_btn = QPushButton("+")
        self.remove_streams_ignored_btn = QPushButton("-")

        self.group_tab = QWidget()
        self.group_list = QListWidget()
        self.add_group_btn = QPushButton("+")
        self.remove_group_btn = QPushButton("-")
        self.group_table = QTableWidget()

        self.group_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.group_table.horizontalHeader().setVisible(False)
        self.group_table.verticalHeader().setVisible(False)
        self.group_table.setColumnCount(2)
        self.group_table.setRowCount(11)

        self.user_tab = QWidget()
        self.user_list = QListWidget()
        self.add_user_btn = QPushButton("+")
        self.remove_user_btn = QPushButton("-")
        self.user_table = QTableWidget()

        self.user_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.user_table.horizontalHeader().setVisible(False)
        self.user_table.verticalHeader().setVisible(False)
        self.user_table.setColumnCount(2)
        self.user_table.setRowCount(6)

        self.protection_tab = QWidget()
        self.protection_list = QListWidget()
        self.add_protection_btn = QPushButton("+")
        self.remove_protection_btn = QPushButton("-")
        self.protection_table = QTableWidget()

        self.protection_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.protection_table.horizontalHeader().setVisible(False)
        self.protection_table.verticalHeader().setVisible(False)
        self.protection_table.setColumnCount(2)
        self.protection_table.setRowCount(6)

        self.typemap_tab = QWidget()
        self.typemap_type_list = QListWidget()
        self.typemap_add_type_btn = QPushButton("+")
        self.typemap_remove_type_btn = QPushButton("-")
        self.typemap_path_list = QListWidget()
        self.typemap_add_path_btn = QPushButton("+")
        self.typemap_remove_path_btn = QPushButton("-")

        self.branch_tab = QWidget()
        self.branch_list = QListWidget()
        self.add_branch_btn = QPushButton("+")
        self.remove_branch_btn = QPushButton("-")
        self.branch_table = QTableWidget()
        self.branch_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.branch_table.horizontalHeader().setVisible(False)
        self.branch_table.verticalHeader().setVisible(False)
        self.branch_table.setColumnCount(2)
        self.branch_table.setRowCount(3)

        self.branch_view_table = QTableWidget()
        self.branch_view_add_path_btn = QPushButton("+")
        self.branch_view_remove_path_btn = QPushButton("-")
        self.branch_view_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.branch_view_table.horizontalHeader().setVisible(False)
        self.branch_view_table.verticalHeader().setVisible(False)
        self.branch_view_table.setColumnCount(2)
        self.branch_view_table.setRowCount(2)

    def add_ui_elements_to_layout(self):

        # Depot Tab
        self.depot_hlayout = QHBoxLayout()
        self.depot_btn_hlayout = QHBoxLayout()
        self.depot_vlayout = QVBoxLayout()

        self.depot_vlayout.addWidget(self.depot_list)
        self.depot_btn_hlayout.addWidget(self.remove_depot_btn)
        self.depot_btn_hlayout.addWidget(self.add_depot_btn)
        self.depot_vlayout.addLayout(self.depot_btn_hlayout)
        self.depot_hlayout.addLayout(self.depot_vlayout)
        self.depot_hlayout.addWidget(self.depot_table)
        self.depot_tab.setLayout(self.depot_hlayout)

        # Streams Tab
        self.stream_vlayout_main = QVBoxLayout()
        self.stream_hlayout = QHBoxLayout()
        self.stream_btn_hlayout = QHBoxLayout()
        self.stream_vlayout = QVBoxLayout()
        
        self.stream_vlayout.addWidget(self.stream_list)
        self.stream_btn_hlayout.addWidget(self.remove_stream_btn)
        self.stream_btn_hlayout.addWidget(self.add_stream_btn)
        self.stream_vlayout.addLayout(self.stream_btn_hlayout)
        self.stream_hlayout.addLayout(self.stream_vlayout)
        self.stream_hlayout.addWidget(self.stream_table)

        self.stream_vlayout_main.addLayout(self.stream_hlayout)
        self.stream_vlayout_main.addWidget(self.stream_view_tab_widget)
        
        self.stream_paths_tab_vlayout = QVBoxLayout()
        self.stream_paths_btn_hlayout = QHBoxLayout()
        self.stream_paths_btn_hlayout.addWidget(self.add_stream_paths_btn )
        self.stream_paths_btn_hlayout.addWidget(self.remove_stream_paths_btn)
        self.stream_paths_tab_vlayout.addWidget(self.stream_paths_list)
        self.stream_paths_tab_vlayout.addLayout(self.stream_paths_btn_hlayout)
        self.stream_paths_tab.setLayout(self.stream_paths_tab_vlayout) 
        self.stream_view_tab_widget.addTab(self.stream_paths_tab, "Paths")
        
        self.stream_remapped_tab_vlayout = QVBoxLayout()
        self.stream_remapped_btn_hlayout = QHBoxLayout()
        self.stream_remapped_btn_hlayout.addWidget(self.add_streams_remapped_btn )
        self.stream_remapped_btn_hlayout.addWidget(self.remove_streams_remapped_btn)
        self.stream_remapped_tab_vlayout.addWidget(self.stream_remapped_table)
        self.stream_remapped_tab_vlayout.addLayout(self.stream_remapped_btn_hlayout)
        self.stream_remapped_tab.setLayout(self.stream_remapped_tab_vlayout) 
        self.stream_view_tab_widget.addTab(self.stream_remapped_tab, "Remapped")

        self.stream_ignored_tab_vlayout = QVBoxLayout()
        self.stream_ignored_btn_hlayout = QHBoxLayout()
        self.stream_ignored_btn_hlayout.addWidget(self.add_streams_ignored_btn )
        self.stream_ignored_btn_hlayout.addWidget(self.remove_streams_ignored_btn)
        self.stream_ignored_tab_vlayout.addWidget(self.stream_ignored_list)
        self.stream_ignored_tab_vlayout.addLayout(self.stream_ignored_btn_hlayout)
        self.stream_ignored_tab.setLayout(self.stream_ignored_tab_vlayout) 
        self.stream_view_tab_widget.addTab(self.stream_ignored_tab, "Ignored")
        
        self.stream_tab.setLayout(self.stream_vlayout_main)

        # Group Tab
        self.group_hlayout = QHBoxLayout()
        self.group_btn_hlayout = QHBoxLayout()
        self.group_vlayout = QVBoxLayout()

        self.group_vlayout.addWidget(self.group_list)
        self.group_btn_hlayout.addWidget(self.remove_group_btn)
        self.group_btn_hlayout.addWidget(self.add_group_btn)
        self.group_vlayout.addLayout(self.group_btn_hlayout)
        self.group_hlayout.addLayout(self.group_vlayout)
        self.group_hlayout.addWidget(self.group_table)
        self.group_tab.setLayout(self.group_hlayout)

        # User Tab
        self.user_hlayout = QHBoxLayout()
        self.user_btn_hlayout = QHBoxLayout()
        self.user_vlayout = QVBoxLayout()

        self.user_vlayout.addWidget(self.user_list)
        self.user_btn_hlayout.addWidget(self.remove_user_btn)
        self.user_btn_hlayout.addWidget(self.add_user_btn)
        self.user_vlayout.addLayout(self.user_btn_hlayout)
        self.user_hlayout.addLayout(self.user_vlayout)
        self.user_hlayout.addWidget(self.user_table)
        self.user_tab.setLayout(self.user_hlayout)

        # Protection Tab
        self.protection_hlayout = QHBoxLayout()
        self.protection_btn_hlayout = QHBoxLayout()
        self.protection_vlayout = QVBoxLayout()

        self.protection_vlayout.addWidget(self.protection_list)
        self.protection_btn_hlayout.addWidget(self.remove_protection_btn)
        self.protection_btn_hlayout.addWidget(self.add_protection_btn)
        self.protection_vlayout.addLayout(self.protection_btn_hlayout)
        self.protection_hlayout.addLayout(self.protection_vlayout)
        self.protection_hlayout.addWidget(self.protection_table)
        self.protection_tab.setLayout(self.protection_hlayout)

        # typemap Tab
        self.typemap_hlayout = QHBoxLayout()
        self.typemap_type_btn_hlayout = QHBoxLayout()
        self.typemap_type_vlayout = QVBoxLayout()
        self.typemap_path_btn_hlayout = QHBoxLayout()
        self.typemap_path_vlayout = QVBoxLayout()

        self.typemap_type_vlayout.addWidget(self.typemap_type_list)
        self.typemap_type_btn_hlayout.addWidget(self.typemap_remove_type_btn)
        self.typemap_type_btn_hlayout.addWidget(self.typemap_add_type_btn)
        self.typemap_type_vlayout.addLayout(self.typemap_type_btn_hlayout)

        self.typemap_path_vlayout.addWidget(self.typemap_path_list)
        self.typemap_path_btn_hlayout.addWidget(self.typemap_remove_path_btn)
        self.typemap_path_btn_hlayout.addWidget(self.typemap_add_path_btn)
        self.typemap_path_vlayout.addLayout(self.typemap_path_btn_hlayout)

        self.typemap_hlayout.addLayout(self.typemap_type_vlayout)
        self.typemap_hlayout.addLayout(self.typemap_path_vlayout)
        self.typemap_tab.setLayout(self.typemap_hlayout)

        # branch Tab
        self.branch_hlayout = QHBoxLayout()
        self.branch_btn_hlayout = QHBoxLayout()
        self.branch_vlayout = QVBoxLayout()
        self.branch_vlayout_main = QVBoxLayout()
        self.branch_view_btn_hlayout = QHBoxLayout()
        self.branch_view_vlayout = QVBoxLayout()

        self.branch_vlayout.addWidget(self.branch_list)
        self.branch_btn_hlayout.addWidget(self.remove_branch_btn)
        self.branch_btn_hlayout.addWidget(self.add_branch_btn)
        self.branch_vlayout.addLayout(self.branch_btn_hlayout)
        self.branch_hlayout.addLayout(self.branch_vlayout)
        self.branch_hlayout.addWidget(self.branch_table)

        self.branch_view_btn_hlayout.addWidget(self.branch_view_remove_path_btn)
        self.branch_view_btn_hlayout.addWidget(self.branch_view_add_path_btn)
        self.branch_view_vlayout.addWidget(self.branch_view_table)
        self.branch_view_vlayout.addLayout(self.branch_view_btn_hlayout)

        self.branch_vlayout_main.addLayout(self.branch_hlayout)
        self.branch_vlayout_main.addLayout(self.branch_view_vlayout)
        self.branch_tab.setLayout(self.branch_vlayout_main)

        # Main Layout
        self.main_layout = QVBoxLayout()

        self.main_btn_row = QHBoxLayout()
        self.main_btn_row.addWidget(self.btn_reload)
        self.main_btn_row.addWidget(self.btn_save)
        
        self.main_tab_widget.addTab(self.depot_tab, "Depots")
        self.main_tab_widget.addTab(self.stream_tab, "Streams")
        self.main_tab_widget.addTab(self.group_tab, "Groups")
        self.main_tab_widget.addTab(self.user_tab, "Users")
        self.main_tab_widget.addTab(self.protection_tab, "Protections")
        self.main_tab_widget.addTab(self.typemap_tab, "Typemap")
        self.main_tab_widget.addTab(self.branch_tab, "Branches")
        self.main_layout.addWidget(self.main_tab_widget)
        self.main_layout.addLayout(self.main_btn_row)

        self.setLayout(self.main_layout)

    def set_window_settings(self):
        self.setWindowTitle("P4 Template Editor")
        self.setMinimumSize(400, 500)

    def populate_depot_data(self):
        if self.template_data.get("depots"):
            for depot in self.template_data["depots"]:
                self.depot_list.addItem(depot["name"])
            self.depot_list.setCurrentRow(0)

            for i, key in enumerate(["name", "type", "depth", "user"]):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.depot_table.setItem(i, 0, key_item)
                self.depot_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["depots"][0].get(
                                key, self.defaults["depot"][key]
                            )
                        )
                    ),
                )

    def populate_group_data(self):
        # Groups
        if self.template_data.get("groups"):
            for group in self.template_data["groups"]:
                self.group_list.addItem(group["name"])
            self.group_list.setCurrentRow(0)

            for i, key in enumerate(
                [
                    "name",
                    "description",
                    "max_results",
                    "max_scan_rows",
                    "max_lock_time",
                    "max_open_files",
                    "timeout",
                    "password_timeout",
                    "subgroups",
                    "owners",
                    "users",
                ]
            ):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.group_table.setItem(i, 0, key_item)
                self.group_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["groups"][0].get(
                                key, self.defaults["group"][key]
                            ),
                            ", ",
                        )
                    ),
                )

    def populate_user_data(self):
        # Users
        if self.template_data.get("users"):
            for user in self.template_data["users"]:
                self.user_list.addItem(user["name"])

            self.user_list.setCurrentRow(0)

            for i, key in enumerate(
                ["name", "email", "full_name", "auth_method", "reviews", "job_view"]
            ):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.user_table.setItem(i, 0, key_item)
                self.user_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["users"][0].get(
                                key, self.defaults["user"][key]
                            ),
                            ", ",
                        )
                    ),
                )

    def populate_stream_data(self):
        # Streams
        if self.template_data.get("streams"):
            for stream in self.template_data["streams"]:
                self.stream_list.addItem(stream["name"])

            self.stream_list.setCurrentRow(0)

            for i, key in enumerate(
                ["name", "type", "depot", "user", "view", "parent", "options"]
            ):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.stream_table.setItem(i, 0, key_item)
                self.stream_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["streams"][0].get(
                                key, self.defaults["stream"][key]
                            ),
                            " ",
                        )
                    ),
                )

    def populate_protection_data(self):
        # Protections
        if self.template_data.get("protections"):
            for protection in self.template_data["protections"]:
                self.protection_list.addItem(protection["name"])

            self.protection_list.setCurrentRow(0)

            for i, key in enumerate(
                ["access", "type", "name", "host", "path", "comment"]
            ):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.protection_table.setItem(i, 0, key_item)
                self.protection_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["protections"][0].get(
                                key, self.defaults["protection"][key]
                            ),
                            " ",
                        )
                    ),
                )

    def populate_typemap_data(self):
        # Types
        if self.template_data.get("types"):
            sorted_types = sorted(self.template_data["types"].keys())
            for typemap in sorted_types:
                self.typemap_type_list.addItem(typemap)

            self.typemap_type_list.setCurrentRow(0)

            for type_path in self.template_data["types"][sorted_types[0]]:
                self.typemap_path_list.addItem(type_path)

    def populate_branch_data(self):
        # Branches
        if self.template_data.get("branches"):
            for branch in self.template_data["branches"]:
                self.branch_list.addItem(branch["name"])

            self.branch_list.setCurrentRow(0)

            for i, key in enumerate(["name", "owner", "options"]):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.branch_table.setItem(i, 0, key_item)
                self.branch_table.setItem(
                    i,
                    1,
                    QTableWidgetItem(
                        convert_to_string(
                            self.template_data["branches"][0].get(
                                key, self.defaults["branch"][key]
                            )
                        )
                    ),
                )

            for i, item in enumerate(
                self.template_data["branches"][0]["view"].items()
            ):

                self.branch_view_table.setItem(i, 0, QTableWidgetItem(item[0]))
                self.branch_view_table.setItem(i, 1, QTableWidgetItem(item[1]))

    def populate_data(self):
        self.template_data = {}
        if self.template_path and os.path.isfile(self.template_path):
            self.template_data = read_json(self.template_path)
        
        self.populate_depot_data()
        self.populate_group_data()
        self.populate_user_data()
        self.populate_stream_data()
        self.populate_protection_data()
        self.populate_typemap_data()
        self.populate_branch_data()

