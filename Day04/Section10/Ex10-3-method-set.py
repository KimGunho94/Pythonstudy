'''
파일명: Ex10-3-method-set.py
'''
# 교집합(&)
s1 = {'apple', 'bananan', 'cherry'}
s2 = {'apple', 'bananan', 'orange'}
print(s1 & s2)
# 메소드
result = s1.intersection(s2)
print(result)

# 합집합(|)
s1 = {'apple', 'bananan', 'cherry'}
s2 = {'apple', 'bananan', 'orange'}
print(s1 | s2)
# 메소드
result = s1.union(s2)
print(result)

# 차집합(-)
s1 = {'apple', 'bananan', 'cherry'}
s2 = {'apple', 'bananan', 'orange'}
print(s1 - s2)
# 메소드
result = s1.difference(s2)
print(result)

