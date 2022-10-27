'''Ex13-9-readHello6.py'''
import sys

file = open('hello.txt', 'rt')

line_list = file.readlines()
sys.stdout.writelines(line_list)

file.close()