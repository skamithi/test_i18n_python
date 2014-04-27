#!/usr/bin/env python

try:
    import DistUtilsExtra.auto
except ImportError:
    import sys
    print >> sys.stderr, 'To build feedie you need https://launchpad.net/python-distutils-extra'
    sys.exit(1)
DistUtilsExtra.auto.setup(
    name="test_i18n",
    version="0.1"
)
