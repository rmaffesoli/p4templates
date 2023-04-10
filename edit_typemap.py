#!/usr/bin/env python

"""edit_permissions doc string"""

from __future__ import print_function

import subprocess

def get_typemap():
    with subprocess.Popen(
        ["p4", "typemap", "-o"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        type_stdout = proc.communicate()[0]

        type_string = type_stdout.decode()
        print(type_string)
        type_string = type_string.split("TypeMap:\r")[1]
        type_string = type_string.replace('\t','')
        type_string = type_string.replace('\n\n','\n')

        raw_type_list = [_ for _ in type_string.split('\r') if _ not in ['', '\n']]
        type_dict = {}

        for entry in raw_type_list:
            while '  ' in entry:
                entry = entry.replace('  ', ' ')

            type_key, type_value = [_.replace('\n', '') for _ in entry.split(' ')]
            
            if type_key not in type_dict:
                type_dict[type_key] = set()

            type_dict[type_key].add(type_value)
        
        return type_dict


def add_type(type_dict, type_key, type_value):
    if type_key not in type_dict:
        type_dict[type_key] = set()

    type_dict[type_key].add(type_value)
    return type_dict


def save_typemap(type_dict):
    # print(type_dict)
    protection_lines = ["TypeMap:"]
    for file_type in sorted(type_dict):
        for file_path in sorted(type_dict[file_type]):
            entry_line = '\t{type} {path}'.format(
                type=file_type,
                path=file_path
            )

            protection_lines.append(entry_line)
    # print('\n'.join(protection_lines))

    with subprocess.Popen(
        ["p4", "typemap", "-i"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:
        prot_stdout = proc.communicate(input=bytes('\n'.join(protection_lines), "utf-8"))[0]
        print(prot_stdout.decode())


def append_new_typemap_entry(type_entries):
    existing_types = get_typemap()
    for file_type in type_entries:
        for file_path in type_entries[file_type]:
            existing_types = add_type(existing_types, file_type, file_path) 
    save_typemap(existing_types)

    
if __name__ == "__main__":
    type_entries={
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
            "//....upk"
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
        ], 
    }
    append_new_typemap_entry(type_entries=type_entries)
    
