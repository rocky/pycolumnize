#/bin/bash
pycolumnize_merge_30_owd=$(pwd)
PYTHON_VERSION=3.0
pyenv local $PYTHON_VERSION
cd $(dirname ${BASH_SOURCE[0]})
if . ./setup-python-3.0.sh; then
    git merge python-3.3-to-3.5
fi
cd $pycolumnize_merge_30_owd
