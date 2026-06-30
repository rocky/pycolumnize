#!/bin/bash
PACKAGE=columnize
PYMODULE_NAME=columnize

# FIXME put some of the below in a common routine
function finish {
  cd $pycolumnize_owd
}

cd $(dirname ${BASH_SOURCE[0]})
pycolumnize_owd=$(pwd)
trap finish EXIT

if ! source ./pyenv-newest-versions ; then
    exit $?
fi

if ! source ./setup-master.sh ; then
    exit $?
fi
cd ..

source $PYMODULE_NAME/version.py
echo $__version__
pyenv local 3.14

rm -fr build
pip wheel --wheel-dir=dist .
python -m build --sdist
finish
