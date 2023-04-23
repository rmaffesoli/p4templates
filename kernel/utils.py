from __future__ import print_function

import json
import re


def set_default(obj):
    """
    Converts any set to a list type object.
    """
    if isinstance(obj, set):
        return list(obj)
    return obj


def write_json(data_dict, output_path, sort_keys=True):
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
    return found_parameters


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

    

if __name__ == "__main__":
    input = read_json(r"C:\repos\p4_templates\kernel\templates\unreal.json")
    # params = gather_parameters(input)
    # print(params)
    replacement = substitute_parameters(input, {"project": "hoodrat"})
    print(replacement)