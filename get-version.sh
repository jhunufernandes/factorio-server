#!/bin/bash

prefix='Version: '

grep "$prefix" factorio/data/changelog.txt | head -n 1 | sed -e "s/^$prefix//"
