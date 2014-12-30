#!/bin/bash
cd '/stash/mm-group/ct101hmax/'
nice -n 19 python -u scripts/test.py < /dev/null &> logfile & disown
