import sys

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
        self.depot_table = QTableWidget()
        self.depot_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.depot_table.horizontalHeader().setVisible(False)
        self.depot_table.verticalHeader().setVisible(False)
        self.depot_table.setColumnCount(2)
        self.depot_table.setRowCount(4)

        self.stream_tab = QWidget()
        self.stream_list = QListWidget()
        self.stream_table = QTableWidget()
        self.stream_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.stream_table.horizontalHeader().setVisible(False)
        self.stream_table.verticalHeader().setVisible(False)
        self.stream_table.setColumnCount(2)
        self.stream_table.setRowCount(7)

        self.group_tab = QWidget()
        self.group_list = QListWidget()
        self.group_table = QTableWidget()
        self.group_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.group_table.horizontalHeader().setVisible(False)
        self.group_table.verticalHeader().setVisible(False)
        self.group_table.setColumnCount(2)
        self.group_table.setRowCount(11)


        self.user_tab = QWidget()
        self.user_list = QListWidget()
        self.user_table = QTableWidget()
        self.user_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.user_table.horizontalHeader().setVisible(False)
        self.user_table.verticalHeader().setVisible(False)
        self.user_table.setColumnCount(2)
        self.user_table.setRowCount(6)

        self.protection_tab = QWidget()
        self.protection_list = QListWidget()
        self.protection_table = QTableWidget()
        self.protection_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.protection_table.horizontalHeader().setVisible(False)
        self.protection_table.verticalHeader().setVisible(False)
        self.protection_table.setColumnCount(2)
        self.protection_table.setRowCount(6)

        self.typemap_tab = QWidget()
        self.typemap_type_list = QListWidget()
        self.typemap_path_list = QListWidget()

        self.branch_tab = QWidget()
        self.branch_list = QListWidget()
        self.branch_table = QTableWidget()
        self.branch_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.branch_table.horizontalHeader().setVisible(False)
        self.branch_table.verticalHeader().setVisible(False)
        self.branch_table.setColumnCount(2)
        self.branch_table.setRowCount(4)

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
        self.typemap_hlayout.addWidget(self.typemap_type_list)
        self.typemap_hlayout.addWidget(self.typemap_path_list)
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
        self.setMinimumSize(400, 500)

    def add_mock_data(self):

        # Template Selection Combo Box
        self.template_cbox.addItem('Unreal')
        self.template_cbox.addItem('Unity')
        self.template_cbox.addItem('Add New Base Template...')
        
        # Depots
        self.depot_list.addItem('unreal_test_depot')
        self.depot_list.setCurrentRow(0)

        self.depot_table.setItem(0, 0, QTableWidgetItem('Name'))
        self.depot_table.setItem(0, 1, QTableWidgetItem('unreal_test_depot'))

        self.depot_table.setItem(1, 0, QTableWidgetItem('Type'))
        self.depot_table.setItem(1, 1, QTableWidgetItem('stream'))
        
        self.depot_table.setItem(2, 0, QTableWidgetItem('Depth'))
        self.depot_table.setItem(2, 1, QTableWidgetItem('1'))
        
        self.depot_table.setItem(3, 0, QTableWidgetItem('User'))
        self.depot_table.setItem(3, 1, QTableWidgetItem('rmaffesoli'))


        # Groups
        self.group_list.addItem('unreal_test_group')
        self.group_list.setCurrentRow(0)

        self.group_table.setItem(0, 0, QTableWidgetItem('Name'))
        self.group_table.setItem(0, 1, QTableWidgetItem('unreal_test_group'))

        self.group_table.setItem(1, 0, QTableWidgetItem('Description'))
        self.group_table.setItem(1, 1, QTableWidgetItem('A group I\'ll be making and deleting often.'))
        
        self.group_table.setItem(2, 0, QTableWidgetItem('Max Results'))
        self.group_table.setItem(2, 1, QTableWidgetItem('unset'))
        
        self.group_table.setItem(3, 0, QTableWidgetItem('Max Scan Rows'))
        self.group_table.setItem(3, 1, QTableWidgetItem('unset'))

        self.group_table.setItem(4, 0, QTableWidgetItem('Max Lock Time'))
        self.group_table.setItem(4, 1, QTableWidgetItem('unset'))

        self.group_table.setItem(5, 0, QTableWidgetItem('Max Open Files'))
        self.group_table.setItem(5, 1, QTableWidgetItem('unset'))

        self.group_table.setItem(6, 0, QTableWidgetItem('Timeout'))
        self.group_table.setItem(6, 1, QTableWidgetItem('43200'))

        self.group_table.setItem(7, 0, QTableWidgetItem('Password Timeout'))
        self.group_table.setItem(7, 1, QTableWidgetItem('unset'))

        self.group_table.setItem(8, 0, QTableWidgetItem('Subgroups'))
        self.group_table.setItem(8, 1, QTableWidgetItem(''))

        self.group_table.setItem(9, 0, QTableWidgetItem('Owners'))
        self.group_table.setItem(9, 1, QTableWidgetItem('rmaffesoli'))

        self.group_table.setItem(10, 0, QTableWidgetItem('Users'))
        self.group_table.setItem(10, 1, QTableWidgetItem('rmaffesoli, test_dude'))

        # Users
        self.user_list.addItem('test_dude')
        self.user_list.setCurrentRow(0)

        self.user_table.setItem(0, 0, QTableWidgetItem('Name'))
        self.user_table.setItem(0, 1, QTableWidgetItem('test_dude'))

        self.user_table.setItem(1, 0, QTableWidgetItem('Email'))
        self.user_table.setItem(1, 1, QTableWidgetItem('test@dude.com'))

        self.user_table.setItem(2, 0, QTableWidgetItem('Full Name'))
        self.user_table.setItem(2, 1, QTableWidgetItem('Test Dude'))

        self.user_table.setItem(3, 0, QTableWidgetItem('Job View'))
        self.user_table.setItem(3, 1, QTableWidgetItem(''))

        self.user_table.setItem(4, 0, QTableWidgetItem('Auth Method'))
        self.user_table.setItem(4, 1, QTableWidgetItem(''))

        self.user_table.setItem(5, 0, QTableWidgetItem('Reviews'))
        self.user_table.setItem(5, 1, QTableWidgetItem(''))

        # Streams
        self.stream_list.addItem('unreal_test_main')
        self.stream_list.addItem('unreal_test_dev')
        self.stream_list.addItem('unreal_test_approval')
        self.stream_list.addItem('unreal_test_task')
        self.stream_list.addItem('unreal_test_dev_virtual')
        self.stream_list.setCurrentRow(0)

        self.stream_table.setItem(0, 0, QTableWidgetItem('Name'))
        self.stream_table.setItem(0, 1, QTableWidgetItem('unreal_test_main'))

        self.stream_table.setItem(1, 0, QTableWidgetItem('Type'))
        self.stream_table.setItem(1, 1, QTableWidgetItem('mainline'))

        self.stream_table.setItem(2, 0, QTableWidgetItem('User'))
        self.stream_table.setItem(2, 1, QTableWidgetItem('rmaffesoli'))

        self.stream_table.setItem(3, 0, QTableWidgetItem('depot'))
        self.stream_table.setItem(3, 1, QTableWidgetItem('unreal_test_depot'))

        self.stream_table.setItem(4, 0, QTableWidgetItem('View'))
        self.stream_table.setItem(4, 1, QTableWidgetItem('inherit'))

        self.stream_table.setItem(5, 0, QTableWidgetItem('parent'))
        self.stream_table.setItem(5, 1, QTableWidgetItem('None'))

        self.stream_table.setItem(6, 0, QTableWidgetItem('Options'))
        self.stream_table.setItem(6, 1, QTableWidgetItem('allsubmit unlocked notoparent nofromparent mergedown'))

        # Protections
        self.protection_list.addItem('unreal_test_group')
        self.protection_list.setCurrentRow(0)

        self.protection_table.setItem(0, 0, QTableWidgetItem('Access'))
        self.protection_table.setItem(0, 1, QTableWidgetItem('write'))

        self.protection_table.setItem(1, 0, QTableWidgetItem('Type'))
        self.protection_table.setItem(1, 1, QTableWidgetItem('group'))

        self.protection_table.setItem(2, 0, QTableWidgetItem('Name'))
        self.protection_table.setItem(2, 1, QTableWidgetItem('unreal_test_group'))

        self.protection_table.setItem(3, 0, QTableWidgetItem('host'))
        self.protection_table.setItem(3, 1, QTableWidgetItem('*'))

        self.protection_table.setItem(4, 0, QTableWidgetItem('path'))
        self.protection_table.setItem(4, 1, QTableWidgetItem("//unreal_test_depot/..."))

        self.protection_table.setItem(5, 0, QTableWidgetItem('Comment'))
        self.protection_table.setItem(5, 1, QTableWidgetItem("auto generated"))
        
        # Branches
        self.branch_list.addItem('unreal_demo_populate')
        self.branch_list.setCurrentRow(0)

        self.branch_table.setItem(0, 0, QTableWidgetItem('Name'))
        self.branch_table.setItem(0, 1, QTableWidgetItem('unreal_demo_populate'))

        self.branch_table.setItem(1, 0, QTableWidgetItem('Owner'))
        self.branch_table.setItem(1, 1, QTableWidgetItem('rmaffesoli'))

        self.branch_table.setItem(2, 0, QTableWidgetItem('Options'))
        self.branch_table.setItem(2, 1, QTableWidgetItem('unlocked'))

        self.branch_table.setItem(3, 0, QTableWidgetItem('View'))
        self.branch_table.setItem(3, 1, QTableWidgetItem('//populate_demo/main/old_project/... //unreal_test_depot/unreal_test_main/new_project/...\n//populate_demo/main/old_project/old_project.py //unreal_test_depot/unreal_test_main/new_project/new_project.py'))

        # Types
        self.typemap_type_list.addItem("binary")
        self.typemap_type_list.addItem("binary+l")
        self.typemap_type_list.addItem("binary+S2w")
        self.typemap_type_list.addItem("text")
        self.typemap_type_list.setCurrentRow(0)

        self.typemap_path_list.addItem("//....bmp")
        self.typemap_path_list.addItem("//....png")
        self.typemap_path_list.addItem("//....tga")
        self.typemap_path_list.addItem("//....raw")
        self.typemap_path_list.addItem("//....r16")
        self.typemap_path_list.addItem("//....mb")
        self.typemap_path_list.addItem("//....fbx")
                

if __name__ == '__main__':
    app = QApplication([])
    P4TemplateEditorDialog() 