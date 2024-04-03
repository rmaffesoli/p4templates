import pytest
from p4_templates.ui.p4_template_loader_gui import P4TemplateLoaderDialog

def test_P4TemplateLoaderDialog_init(mocker):
    m_create_ui_elements = mocker.patch.object(P4TemplateLoaderDialog, 'create_ui_elements')
    m_add_ui_elements_to_layout = mocker.patch.object(P4TemplateLoaderDialog, 'add_ui_elements_to_layout')
    m_connect_ui = mocker.patch.object(P4TemplateLoaderDialog, 'connect_ui')
    m_set_window_settings = mocker.patch.object(P4TemplateLoaderDialog, 'set_window_settings')
    m_reload_ui = mocker.patch.object(P4TemplateLoaderDialog, 'reload_ui')
    m_exec = mocker.patch.object(P4TemplateLoaderDialog, 'exec')
    mocker.patch('p4_templates.ui.p4_template_loader_gui.QDialog')
    m_super = mocker.patch('builtins.super')

    P4TLG = P4TemplateLoaderDialog()

    assert isinstance(P4TLG, P4TemplateLoaderDialog)
    m_create_ui_elements.assert_called_once()
    m_add_ui_elements_to_layout.assert_called_once()
    m_connect_ui.assert_called_once()
    m_set_window_settings.assert_called_once()
    m_reload_ui.assert_called_once()
    m_exec.assert_called_once()
    m_super.assert_called_once()


def test_P4TemplateLoaderDialog_create_ui_elements(mocker):
    return
    mocker.patch.object(P4TemplateLoaderDialog, 'add_ui_elements_to_layout')
    mocker.patch.object(P4TemplateLoaderDialog, 'connect_ui')
    mocker.patch.object(P4TemplateLoaderDialog, 'set_window_settings')
    mocker.patch.object(P4TemplateLoaderDialog, 'reload_ui')
    mocker.patch.object(P4TemplateLoaderDialog, 'exec')
    mocker.patch('p4_templates.ui.p4_template_loader_gui.QDialog')
    mocker.patch('builtins.super')

    m_QComboBox = mocker.patch('p4_templates.ui.p4_template_loader_gui.QComboBox')
    m_QPushButton = mocker.patch('p4_templates.ui.p4_template_loader_gui.QPushButton')
    m_QTableWidget = mocker.patch('p4_templates.ui.p4_template_loader_gui.QTableWidget')

    combo_calls = [mocker.call('nope')]
    push_calls = [mocker.call('nope')]
    table_calls = [mocker.call('nope')]

    P4TLG = P4TemplateLoaderDialog()

    m_QComboBox.assert_has_calls(combo_calls)
    m_QPushButton.assert_has_calls(push_calls)
    m_QTableWidget.assert_has_calls(table_calls)

    




def test_P4TemplateLoaderDialog_update_parameters(mocker):
    pass


def test_P4TemplateLoaderDialog_validate_parameters(mocker):
    pass


def test_P4TemplateLoaderDialog_update_parameters_table(mocker):
    pass


def test_P4TemplateLoaderDialog_update_template_combobox(mocker):
    pass


def test_P4TemplateLoaderDialog_add_ui_elements_to_layout(mocker):
    pass


def test_P4TemplateLoaderDialog_set_window_settings(mocker):
    pass


def test_P4TemplateLoaderDialog_connect_ui(mocker):
    pass


def test_P4TemplateLoaderDialog_edit_current_template(mocker):
    pass


def test_P4TemplateLoaderDialog_edit_new_template(mocker):
    pass


def test_P4TemplateLoaderDialog_process(mocker):
    pass


def test_P4TemplateLoaderDialog_reload_ui(mocker):
    pass