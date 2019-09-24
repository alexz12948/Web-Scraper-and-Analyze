'''
Author: Alexander Zsikla
Name: analyze.py
Date: Fall 2019

Description: Takes in numerous CSV files and outputs a bar graph

'''

import sys
import pandas as pd
import matplotlib
import numpy

if (len(sys.argv) == 1):
    print("Usage: python3 ./analyze.py <CSV File 1> <CSV File 2> ...")
    exit(1)

filenames = []
for i in range(1, len(sys.argv)):
    filenames.append(sys.argv[i])


with open(filenames[0], "r") as csv_file:
    main = pd.read_csv(csv_file)

main.rename(columns={'Letter':'Letter', 
                     'Frequency':'Frequency 1'}, 
                     inplace=True)

for i in range(1, len(filenames)):
    with open(filenames[i], "r") as csv_file:
        df = pd.read_csv(csv_file)

    main[f'Frequency {i + 1}'] = df['Frequency']

print(main)

exit(0)