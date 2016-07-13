#!/bin/bash
ls $@ | while read line; do
	sleep $((RANDOM % 3 + 1))
	echo "$line"
done
