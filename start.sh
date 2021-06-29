#!/bin/sh

TIMEOUT="5s"

while : ; do
  python3 bot.py
  echo "Restarting in $TIMEOUT"
done