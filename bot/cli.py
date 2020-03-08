#!/usr/bin/env python

import argparse

from Toggl.togglApi import getTogglReport

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Obtain report from Toggl.')

    parser.add_argument("--toggl-token", "-tt", help="Set Toggl token.")
    parser.add_argument("--toggl-workspace", "-w", help="Set Toggl workspace")
    parser.add_argument("--since", "-s", help="Start date for the report.")
    parser.add_argument("--until", "-u", help="End date for the report.")

    args = parser.parse_args()

    report = getTogglReport(args.toggl_token, int(args.toggl_workspace), args.since, args.until)

    print(report)
