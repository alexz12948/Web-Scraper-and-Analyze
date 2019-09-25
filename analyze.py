'''
Author: Alexander Zsikla
Name: analyze.py
Date: Fall 2019

Description: Takes in numerous CSV files and outputs a bar graph

'''

import sys
import pandas as pd
from matplotlib import pyplot as plt
import numpy

def get_title(s):
    return s[10:]

if (len(sys.argv) == 1):
    print("Usage: python3 ./analyze.py <CSV File 1> <CSV File 2> ...")
    exit(1)

filenames = []
for i in range(1, len(sys.argv)):
    filenames.append(sys.argv[i])


with open(filenames[0], "r") as csv_file:
    main = pd.read_csv(csv_file)

main.rename(columns={'Letter':'Letter', 
                     'Frequency':'Frequency1'}, 
                     inplace=True)

for i in range(1, len(filenames)):
    with open(filenames[i], "r") as csv_file:
        df = pd.read_csv(csv_file)

    main[f'Frequency{i + 1}'] = df['Frequency']

plt.figure(figsize=(10,5));

for i in range(len(filenames)):
    plt.subplot(1, len(filenames), i + 1)
    plt.bar(main.Letter, main[main.columns[i + 1]])
    plt.title(f"{get_title(filenames[i])}")

plt.show();

exit(0)