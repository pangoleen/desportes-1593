#!/bin/sh
# usage: launch.sh name [train.py args...]   -> logs/name.log, name.pt
cd ~/code-breaking/sega1593 || exit 1
n=$1; shift
setsid nohup ./venv/bin/python -u train.py --out $n.pt "$@" > logs/$n.log 2>&1 < /dev/null &
