#!/bin/sh

# This is a convenience script for use with a non-installed
# version of mempg, such as one cloned from a git repo.

PYTHONPATH=$(pwd) python3 mempg/main.py "$@"
