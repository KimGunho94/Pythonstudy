'''
파일명: Ex06-1-While.py

반복문
    어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용한다.

반복문 종류
    While, for 문

While문
    특징 조건을 만족하는 동안 반복해서 수행하는 코드

while 조건식
    반복싱행문
'''
# while Ture 입력시 무한 반복한다 조심!
n = 10
while n >= 1:
    print(n)
    n -= 1 # n = n -1