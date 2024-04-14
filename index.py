#!/usr/bin/env python3
# main loader

import sys

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.buffer.flush()

with open("main.html", "rb") as fp:
    content = fp.read()

