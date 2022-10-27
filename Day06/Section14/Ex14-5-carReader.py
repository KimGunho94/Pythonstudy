'''
파일명: Ex14-5-carReader.py
'''

import csv

with open('차량관리.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotrchar='"')
    for line in csv_reader:
        print(line)

