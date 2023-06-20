#!/usr/bin/env python

"""create_branch doc string"""

from __future__ import print_function

import argparse
import subprocess


BRANCH_TEMPLATE = """
Branch:	{branch_name}

Description: 
    Created by {owner}

Owner:	{owner}

Options:    {options}

View:    
{view}
"""


def create_branch(
    branch_name=None,
    owner=None,
    options=None,
    view=None
):
    """create_branch doc string"""
    commands = ["p4", "branch", "-i"]

    if isinstance(options, (list, set)):
        options = " ".join(options)

    if isinstance(view, dict):
        view = "".join([f"\t{k} {v}\n" for k,v in view.items()])

    branch_template = BRANCH_TEMPLATE.format(
        branch_name=branch_name,
        owner=owner,
        options=options,
        view=view
    )

    with subprocess.Popen(
        commands,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        branch_stdout = proc.communicate(input=bytes(branch_template, "utf-8"))[0]
        print(branch_stdout.decode())


def populate_branch(branch_name):
    with subprocess.Popen(
        ["p4", "populate", "-b", branch_name],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        branch_stdout = proc.communicate()[0]
        print(branch_stdout.decode())

def delete_branch(branch_name):
    with subprocess.Popen(
        ["p4", "branch", "-d", branch_name],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:
        branch_stdout = proc.communicate()[0]
        print(branch_stdout.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-w", "--owner", default="")
    parser.add_argument("-o", "--options", nargs="*", default=['unlocked'])
    parser.add_argument("-v", "--view", nargs="*", default={})

    parsed_args = parser.parse_args()

    create_branch(
        branch_name=parsed_args.branch_name,
        owner=parsed_args.owner,
        options=parsed_args.options,
        view=parsed_args.view,
    )
