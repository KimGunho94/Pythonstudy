'''
파일명: Ex02-2-variable.py

변수(variable)
    어떤 데이터를 저장하고자 할 떄 사용하는 메모리 저장소.

변수명 규칙
    영문, 한글, 숫자, 밑줄(_)로 구성된다.
    특수 문자(!@#$%^&*()-+ 등) 사용할 수 없다!!
    대 문자와 소 문자를 구분 한다.
    변수명의 첫 글자를 숫자로 사용할 수 없다.
    키워드 (list, dict, if, for, and등)는 사용할 수 없다!!
'''

name = 'Alice'
age = 25
address = ''' 우편번호 610 
경상북도 구미시 고아읍 봉한리
삼우 힐타운 가동 1411호 '''
print(address)

'''
잘못된 변수 명 예시
'''
# Ctrl + / 주석 단축키
# 2myvar = 'Python1'
# my-var = 'Python1'
# my var = 'Python1'

'''
여러 값 할당
    Python을 사용하면 한 줄에 여러 변수에 값을 할당할 수 있다.    
'''

x, y, z = "피카츄", "라이츄", "파이리"
print(x)
print(y)
print(z)

'''
여러 변수에 대한 하나의 값
한 줄에 여러 변수에 동일한 값을 할당할 수 있다.
'''
x = y = z = '꼬부기'
print(x)
print(y)
print(z)