#! /usr/bin/env python2.7

import os

path = "../opentuner/opentuner/utils/adddeps.py"
target = os.path.join(os.path.dirname(__file__), path)

if os.path.isfile(target):
    execfile(target, dict(__file__=target))
