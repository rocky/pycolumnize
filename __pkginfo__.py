"""packaging information"""

import os.path as osp

# Things that change more often go here.
copyright = """
Copyright (C) 2008-2010, 2013, 2015, 2020, 2022 Rocky Bernstein <rocky@gnu.org>.
"""
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Programming Language :: Python :: 2.4",
    "Programming Language :: Python :: 2.5",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.1",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5 ",
    "Programming Language :: Python :: 3.6 ",
    "Programming Language :: Python :: 3.7 ",
    "Programming Language :: Python :: 3.8 ",
    "Programming Language :: Python :: 3.9 ",
    "Programming Language :: Python :: 3.10 ",
]


def get_srcdir():
    filename = osp.normcase(osp.dirname(osp.abspath(__file__)))
    return osp.realpath(filename)


def read(*rnames):
    return open(osp.join(get_srcdir(), *rnames)).read()


exec(read("columnize/version.py"))

# The rest in alphabetic order
author = "Rocky Bernstein"
author_email = "rocky@gnu.org"
license = "MIT"
modname = "columnize"

short_desc = "Format a simple (i.e. not nested) list into aligned columns."
py_modules = [modname]
test_requires = ["pytest"]
web = "https://github.com/rocky/pycolumnize"

readme = "README.txt"
if osp.exists("README.rst"):
    readme = "README.rst"
long_description = read(readme) + "\n"
