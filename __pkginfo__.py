# Copyright (C) 2008 Rocky Bernstein <rocky@gnu.org>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""packaging information"""

modname = 'columnize'

numversion = (0, 1, 0)
version = '.'.join([str(num) for num in numversion])

short_desc = 'Format a list of strings into a single compact string'

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
