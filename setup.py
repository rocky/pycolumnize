#!/usr/bin/env python
"""
distutils setup (setup.py)

This gets a bit of package info from __pkginfo__.py file
"""
from setuptools import find_packages
# Get the required package information
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
      setup_requires     = ['nose>=1.0'],
      test_suite         = "nose.collector",
      url                = web,
      version            = __version__,
      )
