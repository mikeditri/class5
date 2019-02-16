#!/usr/bin/env python

#1. load a data set from a file
#2. "organize" that file, so we can access columns *or* rows of it easily
#3. compute some "summary stats" about the dataset
#4. print the summary stats

#1.load a data set
#1a. accept arbritary filename as argument
#1b. load the file

from argparse import ArgumentParser

parser= ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile', help='path to input file csv file.')

parsed_args = parser.parse_args()
#print(parsed_args)
#print(parsed_args.csvfile)

my_csv_file = parsed_args.csvfile

import os

#if os.path.isfile(my_csv_file):
#    print("Yay, it's real!!!!!!!")
#else:
#    print('Ooops,please give real file')

assert os.path.isfile(my_csv_file) , "please give us a real file"

print('woot the file exists')

#1b. load the file
import pandas as pd

data = pd.read_csv(my_csv_file, header=None)
print(data.head())

#for item in dir(data):
#    print(item)

print(data.shape)






