#!/usr/bin/env python

"""create_stream doc string"""

from __future__ import print_function

import argparse
import os
import subprocess


MAINLINE_TEMPLATE = """
Stream:	//{depot_name}/{stream_name}

Owner:	{user_name}

Name:	{stream_name}

Parent:	{parent_stream}

Type:	{stream_type}

Description:
    Created by {user_name}.

Options:	{options}

ParentView:	{parent_view}

Paths:
    share ...
"""


def create_stream(
    depot_name=None,
    stream_name=None,
    stream_type=None,
    user_name=None,
    parent_view=None,
    parent_stream=None,
):
    """create_stream doc string"""
    commands = ["p4", "stream", "-i"]

    if "//" not in parent_stream:
        parent_stream = "/".join(["/", depot_name, parent_stream])

    if stream_type == "mainline":
        options = "allsubmit unlocked notoparent nofromparent mergedown"
    elif stream_type == "development":
        options = "allsubmit unlocked toparent fromparent mergedown"

    stream_template = MAINLINE_TEMPLATE.format(
        depot_name=depot_name,
        stream_name=stream_name,
        stream_type=stream_type,
        user_name=user_name,
        parent_stream=parent_stream,
        parent_view=parent_view,
        options=options,
    )

    with subprocess.Popen(
        commands,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        stream_stdout = proc.communicate(input=bytes(stream_template, "utf-8"))[0]
        print(stream_stdout.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-d", "--depot", required=True)
    parser.add_argument("-u", "--user", default=os.getenv("P4USER"))
    parser.add_argument("-t", "--type", default="mainline")
    parser.add_argument("-v", "--view", default="inherit")
    parser.add_argument("-p", "--parent", default="none")

    parsed_args = parser.parse_args()

    create_stream(
        depot_name=parsed_args.depot,
        stream_name=parsed_args.name,
        stream_type=parsed_args.type,
        user_name=parsed_args.user,
        parent_view=parsed_args.view,
        parent_stream=parsed_args.parent,
    )
