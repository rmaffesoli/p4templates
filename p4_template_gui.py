import os

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QWidget, 
    QDialog, 
    QPushButton, 
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QListWidget,
    QTableWidget,
    QComboBox,
    QTableWidgetItem,
    QHeaderView
)


class P4TemplateEditorDialog(QDialog):
    def __init__(self, parent=None):
        super(P4TemplateEditorDialog, self).__init__(parent)
        self.create_ui_elements()
        self.add_mock_data()
        self.add_ui_elements_to_layout()
        self.set_window_settings()
        self.exec()

    def create_ui_elements(self):
        self.btn_save_as = QPushButton('Save as...')
        self.btn_save = QPushButton('Save')
        self.btn_run = QPushButton('Run')

        self.main_tab_widget = QTabWidget()
        self.template_cbox = QComboBox()

        self.depot_tab = QWidget()
        
        self.depot_list = QListWidget()
        self.add_depot_btn = QPushButton('+')
        self.remove_depot_btn = QPushButton('-')
        self.depot_table = QTableWidget()

        self.depot_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.depot_table.horizontalHeader().setVisible(False)
        self.depot_table.verticalHeader().setVisible(False)
        self.depot_table.setColumnCount(2)
        self.depot_table.setRowCount(4)

        self.stream_tab = QWidget()
        self.stream_list = QListWidget()
        self.add_stream_btn = QPushButton('+')
        self.remove_stream_btn = QPushButton('-')
        self.stream_table = QTableWidget()

        self.stream_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.stream_table.horizontalHeader().setVisible(False)
        self.stream_table.verticalHeader().setVisible(False)
        self.stream_table.setColumnCount(2)
        self.stream_table.setRowCount(7)

        self.group_tab = QWidget()
        self.group_list = QListWidget()
        self.add_group_btn = QPushButton('+')
        self.remove_group_btn = QPushButton('-')
        self.group_table = QTableWidget()

        self.group_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.group_table.horizontalHeader().setVisible(False)
        self.group_table.verticalHeader().setVisible(False)
        self.group_table.setColumnCount(2)
        self.group_table.setRowCount(11)


        self.user_tab = QWidget()
        self.user_list = QListWidget()
        self.add_user_btn = QPushButton('+')
        self.remove_user_btn = QPushButton('-')
        self.user_table = QTableWidget()

        self.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.user_table.horizontalHeader().setVisible(False)
        self.user_table.verticalHeader().setVisible(False)
        self.user_table.setColumnCount(2)
        self.user_table.setRowCount(6)

        self.protection_tab = QWidget()
        self.protection_list = QListWidget()
        self.add_protection_btn = QPushButton('+')
        self.remove_protection_btn = QPushButton('-')
        self.protection_table = QTableWidget()

        self.protection_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.protection_table.horizontalHeader().setVisible(False)
        self.protection_table.verticalHeader().setVisible(False)
        self.protection_table.setColumnCount(2)
        self.protection_table.setRowCount(6)

        self.typemap_tab = QWidget()
        self.typemap_type_list = QListWidget()
        self.typemap_add_type_btn = QPushButton('+')
        self.typemap_remove_type_btn = QPushButton('-')
        self.typemap_path_list = QListWidget()
        self.typemap_add_path_btn = QPushButton('+')
        self.typemap_remove_path_btn = QPushButton('-')

        self.branch_tab = QWidget()
        self.branch_list = QListWidget()
        self.add_branch_btn = QPushButton('+')
        self.remove_branch_btn = QPushButton('-')
        self.branch_table = QTableWidget()
        self.branch_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.branch_table.horizontalHeader().setVisible(False)
        self.branch_table.verticalHeader().setVisible(False)
        self.branch_table.setColumnCount(2)
        self.branch_table.setRowCount(3)

        self.branch_view_table = QTableWidget()
        self.branch_view_add_path_btn = QPushButton('+')
        self.branch_view_remove_path_btn = QPushButton('-')
        self.branch_view_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
        self.stream_hlayout = QHBoxLayout()
        self.stream_btn_hlayout = QHBoxLayout()
        self.stream_vlayout = QVBoxLayout()

        self.stream_vlayout.addWidget(self.stream_list)
        self.stream_btn_hlayout.addWidget(self.remove_stream_btn)
        self.stream_btn_hlayout.addWidget(self.add_stream_btn)
        self.stream_vlayout.addLayout(self.stream_btn_hlayout)
        self.stream_hlayout.addLayout(self.stream_vlayout)
        self.stream_hlayout.addWidget(self.stream_table)
        self.stream_tab.setLayout(self.stream_hlayout)
    
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
        self.main_btn_row.addWidget(self.btn_save_as)
        self.main_btn_row.addWidget(self.btn_save)
        self.main_btn_row.addWidget(self.btn_run)

        self.main_tab_widget.addTab(self.depot_tab, "Depots")
        self.main_tab_widget.addTab(self.stream_tab, "Streams")
        self.main_tab_widget.addTab(self.group_tab, "Groups")
        self.main_tab_widget.addTab(self.user_tab, "Users")
        self.main_tab_widget.addTab(self.protection_tab, "Protections")
        self.main_tab_widget.addTab(self.typemap_tab, "Typemap")
        self.main_tab_widget.addTab(self.branch_tab, "Branches")
        self.main_layout.addWidget(self.template_cbox)
        self.main_layout.addWidget(self.main_tab_widget)
        self.main_layout.addLayout(self.main_btn_row)

        self.setLayout(self.main_layout)

    def set_window_settings(self):
        self.setWindowTitle("P4 Template Editor")
        self.setMinimumSize(400, 500)

    def add_mock_data(self):
        self.defaults = {
            'depot': {
                'name' : 'None',
                'type' : 'stream',
                'depth' : '1',
                'user' : 'None',
            },
            'group': {
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
                "users": ""
            },
            'user': {
                'name': '',
                'email': '',
                'full_name': '',
                'auth_method': '', 
                'reviews': '', 
                'job_view' : ''
            },
            'stream': {
                'name': '', 
                'type': 'mainline', 
                'depot': '', 
                'user': os.getenv("P4USER"), 
                'view': 'inherit', 
                'parent': '', 
                'options': "allsubmit unlocked notoparent nofromparent mergedown"
            },
            'protection': {
                'access': '', 
                'type': '', 
                'name': '', 
                'host': '*', 
                'path': '', 
                'comment': ''
            },
            'branch': {
                'name': '',
                'owner': '',
                'options': 'unlocked'
            }
        }

        self.current_template_data = {
            "depots": [
                {
                    "name": "unreal_test_depot",
                    "type": "stream",
                    "depth": "1"
                }
            ],
            "groups": [
                {
                    "name": "unreal_test_group",
                    "description": "A group I'll be making and deleting often.",
                    "max_results": "unset",
                    "max_scan_rows": "unset",
                    "max_lock_time": "unset",
                    "max_open_files": "unset",
                    "timeout": "43200",
                    "password_timeout": "unset",
                    "subgroups": "",
                    "owners": [
                        "rmaffesoli"
                    ],
                    "users": [
                        "rmaffesoli",
                        "test_dude"
                    ]
                }
            ],
            "streams": [
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_main"
                },
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_dev",
                    "type": "development",
                    "parent": "unreal_test_main"
                },
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_approval",
                    "type": "development",
                    "parent": "unreal_test_main"
                },
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_dev_2",
                    "type": "development",
                    "parent": "unreal_test_approval",
                    "ignored": [
                        "*.pyc", 
                        ".gitignore", 
                        "/things_i_hate/..."
                    ]
                },
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_task",
                    "type": "task",
                    "parent": "unreal_test_dev"
                },
                {
                    "depot": "unreal_test_depot",
                    "name": "unreal_test_dev_virtual",
                    "type": "virtual",
                    "parent": "unreal_test_dev_2",
                    "paths": [
                        "share ..."
                    ]
                }
            ],
            "users": [
                {
                    "name": "test_dude",
                    "email":"test1@dude.com",
                    "full_name": "test dude"
                }
            ],
            "protections": [
                {
                    "access": "write",
                    "type": "group",
                    "name": "unreal_test_group",
                    "host": "*",
                    "path": "//unreal_test_depot/...",
                    "comment": "auto generated"
                }
            ],
            "branches": [
                {
                    "name": "unreal_demo_populate",
                    "options": [
                        "unlocked"
                    ],
                    "view": {
                        "//populate_demo/main/old_project/...": "//unreal_test_depot/unreal_test_main/new_project/...",
                        "//populate_demo/main/old_project/old_project.py": "//unreal_test_depot/unreal_test_main/new_project/new_project.py"
                    }
                }
            ],
            "types": {
                "binary+S2w": [
                    "//....exe",
                    "//....dll",
                    "//....lib",
                    "//....app",
                    "//....dylib",
                    "//....stub",
                    "//....ipa"
                ],
                "binary+l": [
                    "//....uasset",
                    "//....umap",
                    "//....upk",
                    "//....udk"
                ],
                "binary": [
                    "//....bmp",
                    "//....png",
                    "//....tga",
                    "//....raw",
                    "//....r16",
                    "//....mb",
                    "//....fbx"
                ], 
                "text": [
                    "//....ini",
                    "//....config",
                    "//....cpp",
                    "//....h",
                    "//....c",
                    "//....cs",
                    "//....m",
                    "//....mm",
                    "//....py"        
                ]
            }
        }
 
        # Template Selection Combo Box
        self.template_cbox.addItem('Unreal')
        self.template_cbox.addItem('Unity')
        self.template_cbox.addItem('Add New Base Template...')
        
        # Depots
        if self.current_template_data['depots']:
            for depot in self.current_template_data['depots']:
                self.depot_list.addItem(depot['name'])
            self.depot_list.setCurrentRow(0)

            for i, key in enumerate(['name', 'type', 'depth', 'user']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.depot_table.setItem(i, 0, key_item)
                self.depot_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['depots'][0].get(key, self.defaults['depot'][key]))))

        # Groups
        if self.current_template_data['groups']:
            for group in self.current_template_data['groups']:
                self.group_list.addItem(group['name'])
            self.group_list.setCurrentRow(0)

        for i, key in enumerate(['name', 'description', 'max_results', 'max_scan_rows','max_lock_time', 'max_open_files', 'timeout', 'password_timeout', 'subgroups', 'owners', 'users']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.group_table.setItem(i, 0, key_item)
                self.group_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['groups'][0].get(key, self.defaults['group'][key]), ', ')))

        # Users
        if self.current_template_data['users']:
            for user in self.current_template_data['users']:
                self.user_list.addItem(user['name'])

            self.user_list.setCurrentRow(0)

            for i, key in enumerate(['name', 'email', 'full_name', 'auth_method', 'reviews', 'job_view']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.user_table.setItem(i, 0, key_item)
                self.user_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['users'][0].get(key, self.defaults['user'][key]), ', ')))

        # Streams
        if self.current_template_data['streams']:
            for stream in self.current_template_data['streams']:
                self.stream_list.addItem(stream['name'])

            self.stream_list.setCurrentRow(0)

            for i, key in enumerate(['name', 'type', 'depot', 'user', 'view', 'parent', 'options']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.stream_table.setItem(i, 0, key_item)
                self.stream_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['streams'][0].get(key, self.defaults['stream'][key]), ' ')))

        # Protections
        if self.current_template_data['protections']:
            for protection in self.current_template_data['protections']:
                self.protection_list.addItem(protection['name'])

            self.protection_list.setCurrentRow(0)

            for i, key in enumerate(['access', 'type', 'name', 'host', 'path', 'comment']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.protection_table.setItem(i, 0, key_item)
                self.protection_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['protections'][0].get(key, self.defaults['protection'][key]), ' ')))

        # Types
        if self.current_template_data['types']:
            sorted_types = sorted(self.current_template_data['types'].keys())
            for typemap in sorted_types:
                self.typemap_type_list.addItem(typemap)

            self.typemap_type_list.setCurrentRow(0)

            for type_path in self.current_template_data['types'][sorted_types[0]]:
                self.typemap_path_list.addItem(type_path)

        # Branches
        if self.current_template_data['branches']:
            for branch in self.current_template_data['branches']:
                self.branch_list.addItem(branch['name'])

            self.branch_list.setCurrentRow(0)

            for i, key in enumerate(['name', 'owner', 'options']):
                key_item = QTableWidgetItem(key.capitalize())
                key_item.setFlags(Qt.ItemFlag.ItemIsEditable)
                self.branch_table.setItem(i, 0, key_item)
                self.branch_table.setItem(i, 1, QTableWidgetItem(convert_to_string(self.current_template_data['branches'][0].get(key, self.defaults['branch'][key]))))

            for i, item in enumerate(self.current_template_data['branches'][0]['view'].items()):

                self.branch_view_table.setItem(i, 0, QTableWidgetItem(item[0]))
                self.branch_view_table.setItem(i, 1, QTableWidgetItem(item[1]))


def convert_to_string(input, delimiter=' '):
    if isinstance(input, str):
        return input
    elif isinstance(input, (list, set, tuple)):
        return delimiter.join(input)
    else:
        return str(input)

if __name__ == '__main__':
    app = QApplication([])
    P4TemplateEditorDialog() 