#!/bin/bash

set -e

if [ ! -d venv ]; then
    virtualenv venv
fi

source venv/bin/activate

pip install -U pip
pip install -r requirements.txt

$@
