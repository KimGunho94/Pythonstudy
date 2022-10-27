'''Ex13-7-readHello4.py'''
file = open('hello.txt', 'rt')

line_list = file.readlines()
for line in line_list:
    print(line, end='')

file.close()
