#!/usr/bin/env python
# encoding: utf-8
import sys
from distutils.core import setup
from distutils.util import get_platform

"""
Verify Python platform is Linux
"""
platform = get_platform()
if platform.startswith('linux') == False:
    sys.stderr.write("Daemon-Python is not compatible with %s\n" % platform)
    sys.exit(1)

"""    
Determine appropriate Python version for installation
"""
if sys.version_info[0] >= 3:
    package_dir = {'': 'src/3.x.x'}
else:
    package_dir = {'': 'src/2.x.x'}

setup(
    name = 'daemon',
    version = '0.1',
    description = 'Lightweight and no-nonsense POSIX daemon library for Python (2.x.x/3.x.x)',
    author = 'Fredrick Galoso - Stackd, LLC',
    license = 'MIT/X11',
    platforms='Linux',
    url = 'https://github.com/stackd/daemon-py',
	download_url = 'https://github.com/stackd/daemon-py.git',
    package_dir = package_dir,
    py_modules = [
        'daemon',
    ],
)