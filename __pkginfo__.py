"""packaging information"""

modname = 'columnize'

numversion = (0, 3, 3)
version = '.'.join([str(num) for num in numversion])

short_desc = 'Format a simple (i.e. not nested) list into aligned columns.'

author = "Rocky Bernstein"
author_email = "rocky@gnu.org"

# web = 'http://code.google.com/p/pycolumnize'
# ftp = "ftp://ftp.gnu.org/pub/gnu/libcdio/%s-%s.tar.gz" % (modname, version)
# mailinglist = "mailto:libcdio-pycdio-devel@gnu.org"

classifiers =  ['Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: Python Software Foundation License',
                'Programming Language :: Python',
                'Topic :: Software Development :: Libraries :: Python Modules',
                ]
# download_url = '%s-%s.egg' % (modname, version,)

py_modules = [modname]

web = 'http://code.google.com/p/pycolumnize'
