import sys

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
    QComboBox
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
        self.depot_table = QTableWidget()
        
        self.stream_tab = QWidget()
        self.stream_list = QListWidget()
        self.stream_table = QTableWidget()

        self.group_tab = QWidget()
        self.group_list = QListWidget()
        self.group_table = QTableWidget()

        self.user_tab = QWidget()
        self.user_list = QListWidget()
        self.user_table = QTableWidget()

        self.protection_tab = QWidget()
        self.protection_list = QListWidget()
        self.protection_table = QTableWidget()

        self.typemap_tab = QWidget()
        self.typemap_list = QListWidget()
        self.typemap_table = QTableWidget()

        self.branch_tab = QWidget()
        self.branch_list = QListWidget()
        self.branch_table = QTableWidget()

    def add_ui_elements_to_layout(self):
        
        # Depot Tab
        self.depot_hlayout = QHBoxLayout()
        self.depot_hlayout.addWidget(self.depot_list)
        self.depot_hlayout.addWidget(self.depot_table)
        self.depot_tab.setLayout(self.depot_hlayout)

        # Streams Tab
        self.stream_hlayout = QHBoxLayout()
        self.stream_hlayout.addWidget(self.stream_list)
        self.stream_hlayout.addWidget(self.stream_table)
        self.stream_tab.setLayout(self.stream_hlayout)
    
        # Group Tab
        self.group_hlayout = QHBoxLayout()
        self.group_hlayout.addWidget(self.group_list)
        self.group_hlayout.addWidget(self.group_table)
        self.group_tab.setLayout(self.group_hlayout)

        # User Tab
        self.user_hlayout = QHBoxLayout()
        self.user_hlayout.addWidget(self.user_list)
        self.user_hlayout.addWidget(self.user_table)
        self.user_tab.setLayout(self.user_hlayout)

        # Protection Tab
        self.protection_hlayout = QHBoxLayout()
        self.protection_hlayout.addWidget(self.protection_list)
        self.protection_hlayout.addWidget(self.protection_table)
        self.protection_tab.setLayout(self.protection_hlayout)

        # typemap Tab
        self.typemap_hlayout = QHBoxLayout()
        self.typemap_hlayout.addWidget(self.typemap_list)
        self.typemap_hlayout.addWidget(self.typemap_table)
        self.typemap_tab.setLayout(self.typemap_hlayout)

        # branch Tab
        self.branch_hlayout = QHBoxLayout()
        self.branch_hlayout.addWidget(self.branch_list)
        self.branch_hlayout.addWidget(self.branch_table)
        self.branch_tab.setLayout(self.branch_hlayout)

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
        self.setMinimumSize(400, 800)

    def add_mock_data(self):
        # Depots
        self.depot_list.addItem('unreal_test_depot')

        # Groups
        self.group_list.addItem('unreal_test_group')

        # Users
        self.user_list.addItem('test_dude')

        # Streams
        self.stream_list.addItem('unreal_test_main')
        self.stream_list.addItem('unreal_test_dev')
        self.stream_list.addItem('unreal_test_approval')
        self.stream_list.addItem('unreal_test_task')
        self.stream_list.addItem('unreal_test_dev_virtual')

        # Protections
        self.protection_list.addItem('unreal_test_group')
        
        # Branches
        self.branch_list.addItem('unreal_demo_populate')
        
        # Types
        self.typemap_list.addItem("binary")
        self.typemap_list.addItem("binary+l")
        self.typemap_list.addItem("binary+S2w")
        self.typemap_list.addItem("text")


if __name__ == '__main__':
    app = QApplication([])
    P4TemplateEditorDialog() 