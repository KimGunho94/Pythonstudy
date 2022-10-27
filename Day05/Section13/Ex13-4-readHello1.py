'''
파일명: Ex13-4-readHello1.py
'''
file = open('hello.txt', 'rt')

str = file.read()
print(str, end='')

file.close()