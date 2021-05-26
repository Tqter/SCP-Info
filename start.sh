#!/bin/sh

TIMEOUT="5s"

while : ; do
  python main.py
  echo "Restarting in $TIMEOUT"
done