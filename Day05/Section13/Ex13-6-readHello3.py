'''Ex13-6-readHello3.py'''
file = open('hello.txt', 'rt')

while True:
    str = file.readline()
    if str == '':
        break
    print(str, end='')

file.close()
