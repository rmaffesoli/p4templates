#!/usr/bin/env python

"""create_group doc string"""

from __future__ import print_function

import argparse
import subprocess


GROUP_TEMPLATE = """
Group:	{group_name}

Description: {description}

MaxResults:	{max_results}

MaxScanRows:    {max_scan_rows}

MaxLockTime:    {max_lock_time}

MaxOpenFiles:    {max_open_files}

Timeout:    {timeout}

PasswordTimeout:    {password_timeout}

Subgroups:
{subgroups}

Owners:
{owners}

Users:
{users}
"""


def create_group(
    group_name=None,
    description="",
    max_results="unset",
    max_scan_rows="unset",
    max_lock_time="unset",
    max_open_files="unset",
    timeout="43200",
    password_timeout="unset",
    subgroups="",
    owners="",
    users="",
):
    """create_group doc string"""
    commands = ["p4", "group", "-i"]

    if isinstance(owners, (list, set)):
        owners = "".join([f"    {_}\n" for _ in owners])

    if isinstance(users, (list, set)):
        users = "".join([f"    {_}\n" for _ in users])

    if isinstance(subgroups, (list, set)):
        subgroups = "".join([f"    {_}\n" for _ in subgroups])

    group_template = GROUP_TEMPLATE.format(
        group_name=group_name,
        description=description,
        max_results=max_results,
        max_scan_rows=max_scan_rows,
        max_lock_time=max_lock_time,
        max_open_files=max_open_files,
        timeout=timeout,
        password_timeout=password_timeout,
        subgroups=subgroups,
        owners=owners,
        users=users,
    )

    with subprocess.Popen(
        commands,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        group_stdout = proc.communicate(input=bytes(group_template, "utf-8"))[0]
        print(group_stdout.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-d", "--description")
    parser.add_argument("-m", "--max-results", default="unset")
    parser.add_argument("-r", "--max-scan-rows", default="unset")
    parser.add_argument("-f", "--max-open-files", default="unset")
    parser.add_argument("-l", "--max-lock-time", default="unset")
    parser.add_argument("-t", "--timeout", default="43200")
    parser.add_argument("-p", "--password_timeout", default="unset")
    parser.add_argument("-s", "--subgroups", nargs="*", default="")
    parser.add_argument("-o", "--owners", nargs="*", default="")
    parser.add_argument("-u", "--users", nargs="*", default="")

    parsed_args = parser.parse_args()

    create_group(
        group_name=parsed_args.name,
        description=parsed_args.description,
        max_results=parsed_args.max_results,
        max_scan_rows=parsed_args.max_scan_rows,
        max_lock_time=parsed_args.max_lock_time,
        max_open_files=parsed_args.max_open_files,
        timeout=parsed_args.timeout,
        password_timeout=parsed_args.password_timeout,
        subgroups=parsed_args.subgroups,
        owners=parsed_args.owners,
        users=parsed_args.users,
    )
