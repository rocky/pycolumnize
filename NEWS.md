0.3.11 2022-03-11
=================

Revise for modern Python project organization and practice:
* store source-code module in a directory
* black files
* use pytest
* use `__version__` for version number
* start using github workflows
* Bundle tests into tarball


0.3.10 2020-04-16
=================

Go over portability issues. Is compatible from Python version 2.4..3.8 now

Use TideLift security and make compliant

0.3.9 2016-03-19
================

- Bug fixes

0.3.8 2015-01-13
=================

- Rerelease for PyPI and its f*cking Rst.

0.3.7 2015-01-13
=================

- Get terminal size more portably and reliably (Marc Abramowitz)
- More complete test coverage and testing across python versions, and
  add an additional demo program (Marc Abramowitz)
- README changes, move to github,

0.3.6 2014-22-13
================

- Fix bugs in arrange_array

0.3.5 2014-18-13
================

- Reinstate ability to run on older Pythons. In particular Python
  2.4.6 and 2.5.6 now. I suppose other version in between work too.

- Add opts hash to bundle the growing options old and new:
  * arrange_array
  * arrange_vertical
  * arrange_horizontal
  * array_prefix
  * array_suffix
  * colsep
  * colfmt
  * displaywidth
  * lineprefix
  * linesuffix
  * ljust

- Fixes to make source tarball work. (Added test files properly)

0.3.4 2013-01-03
================

- Make 3k tolerant. This means it no longer works for versions less
  than Python 2.6.

0.3.3 2010-28-10
================

- Work on packaging
- Remove pyflakes warnings
- Correct licensing information

0.3.2 2009-03-08 - Ron Frankel -1 Release
=========================================


- Relax restriction that array has to be string. Now is just something
  we can call str() on each of the elements on.

- Correct bug in vertical alignment

- Add an optional initial line prefix string

0.3.1 2009-01-10 - Sam Woodward Release
=========================================

- Some small typos fixed.

0.3.0 2009-01-05
================


- 0.2.0 had bad bugs - don't use.
  Allow specifying right justification as well as left justification

0.2.0 2008-12-31
================

- Add ability to run columns vertically
