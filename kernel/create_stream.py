#!/usr/bin/env python

"""create_stream doc string"""

from __future__ import print_function

import argparse
import os
import subprocess


STREAM_TEMPLATE = """
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
{paths}

Remapped:
{remapped}

Ignored:
{ignored}

"""


def create_stream(
    depot_name=None,
    stream_name=None,
    user_name="template",
    stream_type="mainline",
    parent_view="inherit",
    parent_stream="none",
    options="",
    paths="    share ...\n",
    remapped="",
    ignored="",
):
    """create_stream doc string"""
    commands = ["p4", "stream", "-i"]

    if parent_stream is not "none" and "//" not in parent_stream:
        parent_stream = "/".join(["/", depot_name, parent_stream])

    if not options:
        if stream_type in ["mainline", "virtual"]:
            options = "allsubmit unlocked notoparent nofromparent mergedown"
        elif stream_type in ["development", "task"]:
            options = "allsubmit unlocked toparent fromparent mergedown"

    if isinstance(paths, (list, set, tuple)):
        paths = "".join([f"    {_}\n" for _ in paths])

    if isinstance(remapped, (list, set, tuple)):
        remapped = "".join([f"    {_}\n" for _ in remapped])

    if isinstance(ignored, (list, set, tuple)):
        ignored = "".join([f"    {_}\n" for _ in ignored])

    stream_template = STREAM_TEMPLATE.format(
        depot_name=depot_name,
        stream_name=stream_name,
        stream_type=stream_type,
        user_name=user_name,
        parent_stream=parent_stream,
        parent_view=parent_view,
        options=options,
        paths=paths,
        remapped=remapped,
        ignored=ignored,
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
    parser.add_argument("-o", "--options", nargs="*", default="")

    parsed_args = parser.parse_args()

    create_stream(
        depot_name=parsed_args.depot,
        stream_name=parsed_args.name,
        stream_type=parsed_args.type,
        user_name=parsed_args.user,
        parent_view=parsed_args.view,
        parent_stream=parsed_args.parent,
        options=parsed_args.options,
    )
