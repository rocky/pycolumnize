#/bin/bash
pycolumnize_merge_30_owd=$(pwd)
PYTHON_VERSION=3.0
pyenv local $PYTHON_VERSION
cd $(dirname ${BASH_SOURCE[0]})
if . ./setup-python-3.0.sh; then
    git merge master
fi
cd $pycolumnize_merge_30_owd
