#!/usr/bin/env python
from __future__ import print_function

import argparse
from datetime import datetime
import os
import subprocess


STREAM_DEPOT_TEMPLATE = """
Depot:	{depot_name}

Owner:	{user_name}

Date:	{creation_date}

Description:
    Created by {user_name}.

Type:	{depot_type}

StreamDepth:	//{depot_name}/{stream_depth}

Map:	{depot_name}/...
"""

LOCAL_DEPOT_TEMPLATE = """

Depot:	{depot_name}

Owner:	{user_name}

Date:	{creation_date}

Description:
    Created by {user_name}.

Type:	{depot_type}

Address:	{depot_type}

Suffix:	.p4s

StreamDepth:	//{depot_name}/{stream_depth}

Map:	{depot_name}/...
"""

GRAPH_DEPOT_TEMPLATE = """
Depot:	{depot_name}

Owner:	{user_name}

Date:	{creation_date}

Description:
    Created by {user_name}.

Type:	{depot_type}

Map:	{depot_name}/...
"""


def create_depot(
    depot_name=None,
    depot_type="stream",
    stream_depth="1",
    user_name=None,
    dryrun=0
):
    commands = ["p4", "depot", "-i"]
    now = datetime.now()
    if not user_name:
        user_name = os.getenv("P4USER")

    if depot_type == "stream":
        depot_template = STREAM_DEPOT_TEMPLATE.format(
            depot_name=depot_name,
            depot_type=depot_type,
            stream_depth=stream_depth,
            user_name=user_name,
            creation_date=now.strftime("%Y/%m/%d %H:%M:%S"),
        )
    elif depot_type == "local":
        depot_template = LOCAL_DEPOT_TEMPLATE.format(
            depot_name=depot_name,
            depot_type=depot_type,
            stream_depth=stream_depth,
            user_name=user_name,
            creation_date=now.strftime("%Y/%m/%d %H:%M:%S"),
        )
    elif depot_type == "graph":
        depot_template = GRAPH_DEPOT_TEMPLATE.format(
            depot_name=depot_name,
            depot_type=depot_type,
            user_name=user_name,
            creation_date=now.strftime("%Y/%m/%d %H:%M:%S"),
        )

    if dryrun:
        print('-'*20)
        print(depot_template)
    else:
        with subprocess.Popen(
            commands,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        ) as proc:

            depot_stdout = proc.communicate(input=bytes(depot_template, "utf-8"))[0]
            print(depot_stdout.decode())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-u", "--user", default=os.getenv("P4USER"))
    parser.add_argument("-t", "--type", default="stream")
    parser.add_argument("-d", "--depth", default="1")

    parsed_args = parser.parse_args()

    create_depot(
        parsed_args.name, parsed_args.type, parsed_args.depth, parsed_args.user
    )
