#!/bin/bash
# Check out 3.3-to-3.5 branch and dependant development branches
PYTHON_VERSION=3.0

if [[ $0 == $${BASH_SOURCE[0]} ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

git checkout python-3.0-to-3.5  && git pull && pyenv local $PYTHON_VERSION
