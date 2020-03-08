#!/usr/bin/env python

import argparse
import os

from Wire.webSocket import runWebsocket

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect to web socket and run.')

    parser.add_argument("--toggl-token", "-tt", help="Set Toggl token.")
    parser.add_argument("--roman-token", "-rt", help="Set  token.")

    args = parser.parse_args()

    os.environ['TOGGL_TOKEN'] = args.toggl_token
    os.environ['ROMAN_TOKEN'] = args.roman_token

    runWebsocket()
