#!/bin/bash

python createflags.py > flags.txt
python caesar.py flags.txt > shiftedwords.csv


