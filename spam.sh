#!/bin/bash
echo "Enter desired amount of messages per hour";
read;
for ((i=0; i<=$REPLY; i++))
do
python3 spamer.py;
sleep $((3600/$REPLY));
done