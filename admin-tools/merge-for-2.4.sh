#/bin/bash
pycolumnize_merge_24_owd=$(pwd)
PYTHON_VERSION=2.4
pyenv local $PYTHON_VERSION
cd $(dirname ${BASH_SOURCE[0]})
if . ./setup-python-2.4.sh; then
    git merge python-3.0-to-3.2
fi
cd $pycolumnize_merge_24_owd
