'''
파일명: Ex04-5-logical.py

논리 연산자
    관계 연산자와 함께 사용되는 연산자로
    2개이상의 항을 논리적으로 연결할 때 사용된다.
'''
a = 10
b = 0 # 0은 false로 0이 아닌숫자는 True로 인식한다.
print('{} > 0 and {} > 0 : {}'.format(a, b, a > 0 and b > 0 ))
print('{} > 0 or {} > 0 : {}'.format(a, b, a > 0 or b > 0 ))
print('not {} : {}'.format(a, not a))
print('not {} : {}'.format(b, not b))
