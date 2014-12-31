#!/bin/bash
cd '/stash/mm-group/ct101hmax/'
nice -n 19 python -u scripts/runall.py < /dev/null &> logfile & disown
