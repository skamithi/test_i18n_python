#!/usr/bin/env python

from flufl.i18n import initialize
import os

os.environ['LANG'] = 'en'
os.environ['LOCPATH'] = './build/mo'
_ = initialize('test_i18n')

with _.using('en'):
    print _("iface.linkstate.admindown")
