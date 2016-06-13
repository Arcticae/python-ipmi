#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import subprocess

name = 'python-ipmi'
version_py = os.path.join(os.path.dirname(__file__), 'pyipmi', 'version.py')
try:
    version = subprocess.Popen(
            ['git', 'describe', '--tags', '--always', '--dirty'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT).communicate()[0].rstrip()
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (OSError, subprocess.CalledProcessError, IOError) as e:
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f, d)
            version = d['__version__']
    except IOError:
        version = 'unknown'

version = version.decode('utf-8')

with open('README.rst') as f:
    readme = f.read()

setup(name = name,
        version = version,
        description = 'Pure python IPMI library',
        long_description = readme,
        url='https://github.com/kontron/python-ipmi',
        download_url = 'https://github.com/kontron/python-ipmi/tarball/' + version,
        author = 'Michael Walle, Heiko Thiery',
        author_email = 'michael.walle@kontron.com, heiko.thiery@kontron.com',
        packages = find_packages(exclude="test"),
        license = 'LGPLv2+',
        platforms = ["any"],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        entry_points = {
            'console_scripts': [
                'ipmitool.py = pyipmi.ipmitool:main',
            ]
        },
        test_suite = 'tests',
)
