#!/usr/bin/env python

"""create_user doc string"""

from __future__ import print_function

import argparse
import subprocess

USER_TEMPLATE = """
User:    {name}

Email:    {email}

FullName:    {full_name}
"""


def create_user(
        name,
        email,
        full_name=None,
        job_view=None,
        auth_method=None,
        reviews=None
):
    """create_user doc string"""
    commands = ["p4", "user", "-fi"]

    if isinstance(full_name, (list, set, tuple)):
        full_name = " ".join(full_name)

    if isinstance(job_view, (list, set, tuple )):
        job_view = "".join([f"    {_}\n" for _ in job_view])

    if isinstance(reviews, (list, set, tuple)):
        reviews = "".join([f"    {_}\n" for _ in reviews])

    if not full_name:
        full_name=name

    user_template = USER_TEMPLATE.format(
        name=name,
        email=email,
        full_name=full_name
    )

    if auth_method:
        user_template = user_template + '\nAuthMethod:    {auth_method}\n'

    if reviews:
        user_template = user_template + '\nReviews:\n{reviews}\n'

    if job_view:
        user_template = user_template + '\nJobView:    {job_view}'

    with subprocess.Popen(
        commands,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    ) as proc:

        user_stdout = proc.communicate(input=bytes(user_template, "utf-8"))[0]
        print(user_stdout.decode())
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True)
    parser.add_argument("-e", "--email", required=True)
    parser.add_argument("-f", "--full_name", nargs="*", default="")
    parser.add_argument("-a", "--auth_method", default="")
    parser.add_argument("-r", "--reviews", nargs="*", default="")
    parser.add_argument("-j", "--job_view", nargs="*", default="")

    parsed_args = parser.parse_args()

    create_user(
        name=parsed_args.name,
        email=parsed_args.email,
        full_name=parsed_args.full_name,
        job_view=parsed_args.job_view,
        auth_method=parsed_args.auth_method,
        reviews=parsed_args.reviews
    )
