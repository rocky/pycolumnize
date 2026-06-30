#!/bin/bash
# Check out 3.3-to-3.5 branch and dependant development branches

bs=${BASH_SOURCE[0]}
if [[ $0 == $bs ]] ; then
    echo "This script should be *sourced* rather than run directly through bash"
    exit 1
fi

PYTHON_VERSION=3.3

export PATH=$HOME/.pyenv/bin/pyenv:$PATH
pytracer_owd=$(pwd)
mydir=$(dirname $bs)
cd $mydir
. ./checkout_common.sh
(cd $fulldir/.. && \
     setup_version python-spark python-3.3 && \
     setup_version python-xdis python-3.3 && \
     setup_version python-filecache python-3.3 && \
     setup_version pycolumnize python-3.0 && \
     setup_version python-uncompyle6 python-3.3 \
    )
cd $pytracer_owd
rm -v */.python-version 2>/dev/null || true

checkout_finish python-3.3-to-3.5
