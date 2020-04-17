#!/usr/bin/env python
"""
distutils setup (setup.py)

This gets a bit of package info from __pkginfo__.py file
"""
# Get the required package information
from __pkginfo__ import \
    author,           author_email,       classifiers,      ftp_url,      \
    license,          long_description,   mailing_list,                   \
    modname,          py_modules,                                         \
    short_desc,       tests_require,      VERSION, web, zip_safe

from setuptools import setup

install_requires = []

import sys
if (2,6) <= sys.version_info < (3, 3):
    install_requires.append('backports.shutil_get_terminal_size')

setup(
      author             = author,
      author_email       = author_email,
      classifiers        = classifiers,
      description        = short_desc,
      license            = license,
      long_description   = long_description,
      long_description_content_type = "text/x-rst",
      name               = modname,
      test_suite         = 'nose.collector',
      url                = web,
      version            = VERSION,
      py_modules         = py_modules,
      install_requires   = install_requires,
      tests_require      = tests_require,
      setup_requires     = ['nose>=1.0'],
      zip_safe           = zip_safe
      )
