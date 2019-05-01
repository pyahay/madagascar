#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Package meta-data
NAME = "madagascar"
DESCRIPTION = "A package for geophysical data processing"
URL = "https://github.com/pyahay/madagascar"
AUTHOR = "Madagascar develop tem"
VERSION = "0.1.0"

REQUIREMENTS = ["numpy"]

# Open README.md and use it as the long-description.
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    url=URL,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
