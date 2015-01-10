![Downloads](https://pypip.in/download/columnize/badge.svg) [![Build Status](https://travis-ci.org/rocky/python2-trepan.svg)](https://travis-ci.org/rocky/columnize/) [![Latest Version](https://pypip.in/version/columnize/badge.svg?text=version)](https://pypi.python.org/pypi/columnize/) [![Supported Python versions](https://pypip.in/py_versions/columnize/badge.svg)](https://pypi.python.org/pypi/columnize/)

In showing a long lists, sometimes one would prefer to see the value arranged aligned in columns. Some examples include listing methods of an object, listing debugger commands, or showing a numeric array with data aligned.

This is a Python module to format a simple (i.e. not nested) list into aligned columns. A string with embedded newline characters is returned.

Setup
-----

```python
$ python
>>> import columnize
```

With String data
----------------

Each column is only as wide as necessary. By default, columns are
separated by two spaces; one was not legible enough. Set *colsep* to
adjust the string separate columns. Set *displaywidth* to set the line
width.

```python
>>> g = ('bibrons', 'golden', 'madascar', 'leopard', 'mourning', 'suras', 'tokay')
>>> print(columnize.columnize(g, displaywidth=15)
bibrons   suras
golden    tokay
madascar
leopard
mourning

>>> print(columnize.columnize(g, displaywidth=19, colsep=' | '))
bibrons  | suras
golden   | tokay
madascar
leopard
mourning

>>> print(columnize.columnize(g, displaywidth=18, colsep=' | ', ljust=False))
bibrons  | mourning
golden   | suras
madascar | tokay
leopard
```

Normally, consecutive items go down from the top to bottom from the left-most column to the right-most. If *arrange_vertical* is set false, consecutive items will go across, left to right, top to bottom.

With numeric data
-----------------

```python
>>> print(columnize.columnize(['1', '2', '3', '4'], displaywidth=6)) # => '1  3\n2  4\n')
1  3
2  4

>>> print(columnize.columnize(list(range(1,6)), displaywidth=8))
1  3  5
2  4
```

By default entries are left justified:

```python
>>>  print(columnize.columnize(list(range(1,16)), displaywidth=10))

1  6   11
2  7   12
3  8   13
4  9   14
5  10  15
```
but you can change that with *ljust* or if *arrange_array* is set to *True*:

```python
>>>  print(columnize.columnize(list(range(1,16)), displaywidth=10, ljust=False))
1   6  11
2   7  12
3   8  13
4   9  14
5  10  15

>>> print(columnize.columnize(list(range(1,5)), opts={'arrange_array':True, 'displaywidth':6}))
[1, 2
 3, 4]


```

Credits
-------

This module (essentially one function) was adapted from a private
method of the same name from Python’s
[cmd](http://docs.python.org/library/cmd.html) module. Some
adjustments and generalizations have been made.

Other stuff
-----------

Authors:   Rocky Bernstein <rockyb@rubyforge.org> [![endorse](https://api.coderwall.com/rocky/endorsecount.png)](https://coderwall.com/rocky)

License: MIT
