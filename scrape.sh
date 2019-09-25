#!/bin/sh

: '
Author: Alexander Zsikla
Project: web_scrape.py
Date: Fall 2019

Description: Takes in a URL and creates a csv file with the name of the domain
and moves it into a folder called CSV_Files

'

if [ $# == 0 ]; then
	echo "Usage: $0 <URL> <Optional: -A (analyze)>"
	exit 0
fi

mkdir CSV_Files

for URL in $@; do
	if [ $URL != "-A" ]; then
		python3 ./web_scrape.py $URL
	fi
done

mv *csv CSV_Files/

flag=0
for phrase in $@; do
	if [ $phrase == "-A" ]; then
		flag=1
	fi
done

if [ $flag == 1 ]; then
	python3 ./analyze.py CSV_Files/*csv
fi