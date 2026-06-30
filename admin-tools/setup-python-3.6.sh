#!/bin/bash
# Check out 3.6-to-3.10 branch and dependant development branches

bs=${BASH_SOURCE[0]}
if [[ $0 == $bs ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

PYTHON_VERSION=3.6

export PATH=$HOME/.pyenv/bin/pyenv:$PATH
pytracer_owd=$(pwd)
mydir=$(dirname $bs)
cd $mydir
. ./checkout_common.sh

checkout_finish python-3.6-to-3.10
