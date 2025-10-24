#!/usr/bin/env python
"""
distutils setup (setup.py)

This gets a bit of package info from __pkginfo__.py file
"""
# Get the required package information
from setuptools import find_packages, setup

from __pkginfo__ import (
    __version__,
    author,
    author_email,
    classifiers,
    license,
    long_description,
    modname,
    py_modules,
    short_desc,
    web,
)

import sys
if sys.version_info[:2] == (3, 0):
    setup_requires = []
    test_suite = None
else:
    setup_requires = ["nose>=1.0"]
    test_suite = "nose.collector"

from setuptools import setup

install_requires = []

setup(
      author             = author,
      author_email       = author_email,
      classifiers        = classifiers,
      description        = short_desc,
      install_requires   = install_requires,
      license            = license,
      long_description   = long_description,
      name               = modname,
      packages=find_packages(),
      py_modules         = py_modules,
      setup_requires     = setup_requires,
      test_suite         = test_suite,
      url                = web,
      version            = __version__,
      )
