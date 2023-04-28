from __future__ import print_function

import json
import re
import os


def set_default(obj):
    """
    Converts any set to a list type object.
    """
    if isinstance(obj, set):
        return list(obj)
    return obj


def write_json(data_dict, output_path, sort_keys=False):
    """
    Writes a dictionary into a json file.
    """
    with open(output_path, "w") as outfile:
        json.dump(
            data_dict, outfile, default=set_default, indent=4, sort_keys=sort_keys
        )


def read_json(json_path):
    """
    Reads a json file in to a dictionary.
    """
    with open(json_path) as json_file:
        data_dict = json.load(json_file)
    return data_dict


def gather_parameters(input, found_parameters=None):
    if isinstance(input, dict):
        input = json.dumps(
            input, default=set_default, indent=4, sort_keys=True
        )
    found_parameters = found_parameters or set()
    matches = re.findall("({[^\{\}\"]*})", input)
    found_parameters = found_parameters.union({_.replace('}','').replace('{','') for _ in matches})
    return sorted(found_parameters)


def substitute_parameters(template, parameters):
    if isinstance(template, dict):
        template = json.dumps(
            template, default=set_default, indent=4, sort_keys=True
        )
    for param, value in parameters.items():
        pattern = '{' + param +'}'
        template = re.sub(pattern, value, template)
    template = json.loads(template)
    return template


def convert_to_string(input, delimiter=" "):
    if isinstance(input, str):
        return input
    elif isinstance(input, (list, set, tuple)):
        return delimiter.join(input)
    else:
        return str(input)


def gather_existing_template_names(template_folder_path="./templates"):
    template_lut = {}
    if os.path.isdir(template_folder_path):
        for dir_name, _, files in os.walk(template_folder_path):
            files = [_ for _ in files if _.lower().endswith('.json')]
            for template_file in files:
                identifier = template_file.replace('.json', '')
                template_data = read_json(os.path.join(dir_name, template_file))
                template_name = template_data.get('name', '')
                
                if template_name and template_name not in template_lut:
                    identifier = template_name
                
                template_lut[identifier] = os.path.join(dir_name, template_file)

    return template_lut