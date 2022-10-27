'''
파일명: Ex10-1-method-string.py

메소드(Method) 란
    특정 객체가 가지고 있는 함수를 의미한다.
'''

# string 객체 format 메소드
s = "10자리 폭 왼쪽 정열 '{:<10d}'"
print(s.format(123)) # 이런식으로도 가능
print("10 자리 폭 왼쪽 정렬 '{:<10d}'".format(123))
print("10 자리 폭 오른쪽 정렬 '{:>10d}'".format(123))
print("10 자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼쪽 정렬 채움문자'{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자'{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자'{:*^10d}'".format(123))

# count()
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다.'
result = s.count('기린')
print(result)

s = 'best of best'
result = s.count('best', 5)
print(result)
result = s.count('best', -7)
print(result)

# find() 메소드 위치한 인덱스 번호 반환
s = 'apple'
result = s.find('p')
print(result)
# 없는 값 입력시 -1로 나온다.
result = s.find('z')
print(result)

s = 'best of best'
result = s.find('best', 5)
print(result)
result = s.find('best', -7)
print(result)

# index() - find()메소드와 같지만 문자열이 존재하지 않을 경우 에러가 발생한다. 예)에러가 발생해야 할 떄 사용 한다.
s = 'apple'
result = s.index('p')
print(result)
s = 'apple'
result = s.index('z')
print(result)