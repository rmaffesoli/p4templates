import pytest

from p4_templates.kernel.utils import load_server_config, setup_server_connection, set_default, write_json, read_json, gather_parameters, substitute_parameters, convert_to_string, gather_existing_template_names


def test_load_server_config(mocker):
    m_read_json = mocker.patch('p4_templates.kernel.utils.read_json')
    
    load_server_config('a/fake/config/path.json')
    
    m_read_json.assert_called_once_with('a/fake/config/path.json')

def test_setup_server_connection():
    pass


def test_set_default():
    pass


def test_write_json():
    pass


def test_read_json():
    pass


def test_gather_parameters():
    pass


def test_substitute_parameters():
    pass


def test_convert_to_string():
    pass


def test_gather_existing_template_names():
    pass