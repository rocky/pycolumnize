|Pypi Installs| |Supported Python Versions|

|packagestatus|

In showing a long lists, sometimes one would prefer to see the value
arranged aligned in columns. Some examples include listing methods of an
object, listing debugger commands, or showing a numeric array with data
aligned.

This is a Python module to format a simple (i.e. not nested) list into
aligned columns. A string with embedded newline characters is returned.

Setup
-----

.. code:: python

    $ python
    >>> import columnize

With String data
----------------

Each column is only as wide as necessary. By default, columns are
separated by two spaces; one was not legible enough. Set *colsep* to
adjust the string separate columns. Set *displaywidth* to set the line
width.

.. code:: python

    >>> g = ('bibrons', 'golden', 'madascar', 'leopard', 'mourning', 'suras', 'tokay')
    >>> print(columnize.columnize(g, displaywidth=15))
    bibrons   suras
    golden    tokay
    madascar
    leopard
    mourning

    >>> print(columnize.columnize(g, displaywidth=19, colsep=' | '))
    bibrons  | mourning
    golden   | suras
    madascar | tokay
    leopard

    >>> print(columnize.columnize(g, displaywidth=18, colsep=' | ', ljust=False))
    bibrons | suras
     golden | tokay
    madascar
     leopard

Normally, consecutive items go down from the top to bottom from the
left-most column to the right-most. If *arrange\_vertical* is set false,
consecutive items will go across, left to right, top to bottom.

With numeric data
-----------------

.. code:: python

    >>> print(columnize.columnize(['1', '2', '3', '4'], displaywidth=6)) # => '1  3\n2  4\n'
    1  3
    2  4

    >>> print(columnize.columnize(list(range(1,6)), displaywidth=8))
    1  3  5
    2  4

By default entries are left justified:

.. code:: python

    >>>  print(columnize.columnize(list(range(1,16)), displaywidth=10))

    1  6   11
    2  7   12
    3  8   13
    4  9   14
    5  10  15

but you can change that with *ljust* or if *arrange\_array* is set to
*True*:

.. code:: python

    >>>  print(columnize.columnize(list(range(1,16)), displaywidth=10, ljust=False))
    1   6  11
    2   7  12
    3   8  13
    4   9  14
    5  10  15

    >>> print(columnize.columnize(list(range(1,5)), opts={'arrange_array':True, 'displaywidth':6}))
    [1, 2
     3, 4]

Credits
-------

This module (essentially one function) was adapted from a private method
of the same name from Python's
`cmd <http://docs.python.org/library/cmd.html>`__ module. Some
adjustments and generalizations have been made.

pycolumnize for enterprise
==========================

Available as part of the Tidelift Subscription.

The maintainers of pycolumnize and thousands of other packages are working with Tidelift to deliver commercial support and maintenance for the open source dependencies you use to build your applications. Save time, reduce risk, and improve code health, while paying the maintainers of the exact dependencies you use. `Learn more. <https://tidelift.com/subscription/pkg/pypi-columnize?utm_source=pypi-columnize&utm_medium=referral&utm_campaign=enterprise&utm_term=repo>`_

Security contact information
============================

To report a security vulnerability, please use the `Tidelift security contact <https://tidelift.com/security>`_ and Tidelift will coordinate the fix and disclosure.

Other stuff
-----------

Authors: Rocky Bernstein rb@dustyfeet.com

License: MIT

.. |Supported Python Versions| image:: https://img.shields.io/pypi/pyversions/columnize.svg
   :target: https://pypi.python.org/pypi/columnize/
.. |Pypi Installs| image:: https://pepy.tech/badge/columnize
.. |packagestatus| image:: https://repology.org/badge/vertical-allrepos/python:columnize.svg
		 :target: https://repology.org/project/python:columnize/versions
