#!/usr/bin/env python

"""edit_permissions doc string"""

from __future__ import print_function

import subprocess
from pprint import pprint



def get_protections_table():
    with subprocess.Popen(
        ["p4", "protect", "-o"],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        perm_stdout = proc.communicate()[0]

        perm_table_string = perm_stdout.decode()
        perm_table_string = perm_table_string.replace("\r", "\n")
        perm_table_string = perm_table_string.replace("\n\n", "\n")            
        perm_table_string = perm_table_string.replace("\t", "")
        perm_table_string = perm_table_string.split("Protections:\n")[2]
        
        raw_perm_table_list = [
            _ for _ in perm_table_string.split("\n") if _ not in ["", "\n"]
        ]
        perm_table_list = []

        for entry in raw_perm_table_list:
            comment = ""
            if "## " in entry:
                entry, comment = entry.split("## ")
            while "  " in entry:
                entry = entry.replace("  ", " ")

            entry_split = [_.replace("\n", "") for _ in entry.split(" ")]
            if len(entry_split) < 5:
                continue
            perm_table_list.append(
                {
                    "access": entry_split[0],
                    "type": entry_split[1],
                    "name": entry_split[2],
                    "host": entry_split[3],
                    "path": entry_split[4],
                    "comment": comment,
                }
            )

        return perm_table_list


def prepend_protection(protections_table, permission):
    if permission not in protections_table:
        protections_table.insert(0, permission)
    else:
        print("protection already exists in table:", permission)
    
    return protections_table


def save_protections_table(protections_table, dryrun=0):
    protection_lines = ["Protections:"]
    for entry in protections_table:
        entry_line = "\t{access} {type} {name} {host} {path}".format(
            access=entry["access"],
            type=entry["type"],
            name=entry["name"],
            host=entry["host"],
            path=entry["path"],
        )
        if entry["comment"]:
            entry_line = entry_line + "\t## {}".format(entry["comment"])

        protection_lines.append(entry_line)

    if dryrun:
        print('='*40)
        print("Projected protection table edits:") 
        print('\n'.join(protection_lines))
        print('='*40)
    else:
        with subprocess.Popen(
            ["p4", "protect", "-i"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ) as proc:
            prot_stdout = proc.communicate(
                input=bytes("\n".join(protection_lines), "utf-8")
            )[0]
            print(prot_stdout.decode())


def append_new_protections(protections, dryrun=0):
    existing_protections = get_protections_table()
    for protection in protections:
        existing_protections = prepend_protection(existing_protections, protection)
    save_protections_table(existing_protections, dryrun)
