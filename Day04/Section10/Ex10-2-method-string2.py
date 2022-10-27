'''
파일명: Ex10-2-method-string2.py
'''
# join() 메소드
s = '-'.join('Python')
print(s)

s = '+'.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)

s = ''.join({'a': 'apple', 'b': 'banana'})
print(s)

# split() 메소드
s = 'list is too short'
result = s.split()
print(result)

s = '010-1234-5678'
result = s.split('-')
print(result)
print(result[2])

# replace() = 변환해준다.
s = 'life is too short'
result = s.replace('short', 'long')
print(result)

#  strip(), lstrip(), rstrip() 공백제거
# 왼쪽 공백 제거
s = '      apple'
print(s)
result = s.lstrip()
print(result)

# 오른쪽 공백 제거
s = 'apple        '
print(s)
result = s.rstrip()
print(result)
# 앞뒤 공백 제거
s = '      apple        '
print(s)
result = s.strip()
print(result)

# 전체 공백 제거
s = ' a p p l e '
print(s)
result = s.replace(' ', '')
print(result)