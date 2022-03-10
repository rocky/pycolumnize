# Compatibility for us old-timers.

# Note: This makefile include remake-style target comments.
# These comments before the targets start with #:
# remake --tasks to shows the targets and the comments

PHONY=check check-full check3 check-short check-short2 check-short3 clean dist distclean test
GIT2CL ?= git2cl
PYTHON ?= python
PYTHON3 ?= python3
LINT    = flake8

#: the default target - same as running "check"
all: check

#: Run tests (one version of Python)
check:
	pytest test

#: Clean up temporary files
clean:
	$(PYTHON) ./setup.py $@

#: Create source (tarball) and binary (egg) distribution
dist: README.rst
	$(PYTHON) -m build

#: Create source tarball
sdist: README.rst
	$(PYTHON) -m build --sdist

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
