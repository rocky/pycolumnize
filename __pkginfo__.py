"""packaging information"""
# Things that change more often go here.
copyright   = '''
Copyright (C) 2008-2010, 2013, 2015, 2022 Rocky Bernstein <rocky@gnu.org>.
'''
classifiers =  ['Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: Python Software Foundation License',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules',
                'Programming Language :: Python :: 2.4',
                'Programming Language :: Python :: 2.5',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.0',
                'Programming Language :: Python :: 3.1',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5 ',
                'Programming Language :: Python :: 3.6 ',
                'Programming Language :: Python :: 3.7 ',
                'Programming Language :: Python :: 3.8 ',
                'Programming Language :: Python :: 3.9 ',
                'Programming Language :: Python :: 3.10 ',
                ]

# The rest in alphabetic order
author       = "Rocky Bernstein"
author_email = "rocky@gnu.org"
ftp_url      = None
license      = "PSF2"
mailing_list = None
modname      = "columnize"

short_desc = 'Format a simple (i.e. not nested) list into aligned columns.'
py_modules = [modname]

# VERSION.py sets variable VERSION.
import os.path as osp
version_file = osp.join(
    osp.dirname(__file__),
    "columnize",
    "version.py")
exec(
    compile(
        open(version_file, "r").read(),
        version_file,
        "exec",
        )
    )

web = 'https://github.com/rocky/pycolumnize'
# tracebacks in zip files are funky and not debuggable
zip_safe = False

def read(*rnames):
    return open(osp.join(osp.dirname(__file__), *rnames)).read()

readme = 'README.txt'
if osp.exists('README.rst'): readme = 'README.rst'
long_description   = ( read(readme) + '\n' )
