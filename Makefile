# Compatibility for us old-timers.

# Note: This makefile include remake-style target comments.
# These comments before the targets start with #:
# remake --tasks to shows the targets and the comments

PHONY=check check-3.0 check-3.1 check-3.2 check-3.3 check-3.4 check-3.5 check-full check3 check-short check-short2 check-short3 clean dist distclean test
GIT2CL ?= git2cl
PYTHON ?= python
PYTHON3 ?= python3
RM ?= rm
LINT    = flake8

PYTHON_VERSION = $(shell $(PYTHON) -V 2>&1 | cut -d ' ' -f 2 | cut -d'.' -f1,2 | head -1)

#: the default target - same as running "check"
all: check

#: Run tests (one version of Python)
check:
	$(MAKE) check-${PYTHON_VERSION}

check-3.0 check-2.4 check-2.5 check-2.6 check-2.7:
	$(PYTHON) test/test_columnize.py

check-3.1 check-3.2 check-3.3 check-3.4 check-3.5 check-3.6 check-3.7 check-3.8 check-3.9:
	$(PYTHON) ./setup.py nosetests

check-short:
	$(PYTHON) ./setup.py nosetests --quiet | \
	$(PYTHON) ./make-check-filter.py
#
# check-short3:
# 	$(PYTHON3) ./setup.py nosetests --quiet | \
# 	$(PYTHON3) ./make-check-filter.py

#: Clean up temporary files
clean:
	$(PYTHON) ./setup.py $@
	$(RM) *.so */*.so || /bin/true

#: Create source (tarball) and binary (egg) distribution
dist: README.rst
	$(PYTHON) -m build

#: Create source tarball
sdist: README.rst
	$(PYTHON) -m build --sdist

# #: Run mypy
# mypy:
# 	mypy columnize

# #: Run mypyc
# mypyc: mypy
# 	mypyc columnize

#: Style check. Set env var LINT to pyflakes, flake, or flake8
lint: flake8

#: Lint program
flake8:
	$(LINT) columnize

#: Create binary egg distribution
bdist_egg: README.rst
	$(PYTHON) ./setup.py bdist_egg

# It is too much work to figure out how to add a new command to distutils
# to do the following. I'm sure distutils will someday get there.
DISTCLEAN_FILES = build dist *.egg-info *.pyc *.so py*.py

#: Remove ALL dervied files
distclean: clean
	-rm -fr $(DISTCLEAN_FILES) || true

#: Install package locally
install:
	$(PYTHON) ./setup.py install

#: Same as 'check' target
test: check

rmChangeLog:
	rm ChangeLog || true

#: Create a ChangeLog from git via git log and git2cl
ChangeLog: rmChangeLog
	git log --pretty --numstat --summary | $(GIT2CL) >$@

.PHONY: $(PHONY)
