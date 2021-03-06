#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo

"""
This is an example of py2app setup.py script for freezing your pywebview
application

Usage:
    python setup.py py2app
"""

import os
from setuptools import setup

DIR = os.path.abspath(os.path.dirname(__file__))

icon_path = os.path.join(DIR, 'icons/b.icns')


def tree(src):
    return [(root, map(lambda f: os.path.join(root, f), files))
            for (root, dirs, files) in os.walk(os.path.normpath(src))]


ENTRY_POINT = ['app.py']

DATA_FILES = tree('DATA_FILES_DIR') + tree('DATA_FILE_DIR2')
OPTIONS = {'argv_emulation': False,
           'strip': True,
           'iconfile': icon_path,
           'plist': {'CFBundleShortVersionString': '0.1.0', },
           # 'iconfile': 'icon.icns', # uncomment to include an icon
           'includes': ['WebKit', 'Foundation', 'webview']}

setup(
    app=ENTRY_POINT,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)