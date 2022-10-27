'''
파일명: Ex02-3-type.py

내장 데이터 유형
Python 변수는 다른 유형의 date 를 저장할 수 있으며
다른 유형은 다른 작업을 수행할 수 있다.
Python 에는 이런한 범주에 기본 적으로 다음 데이터 유형이 내장 되어 있다.

텍스트 유형 : str
숫자 유형 : int, float, complex
시퀸스 유형 : list, tuple, rage
매핑 유형 : dict
세트 유형 : set, frozenset
부울(논리) 유형 : bool
바이너리 유형 : bytes, bytearray, memiryview
없음 유형 : noneType
'''
x = "Hello World"
print(type(x))
# int
x = 20
print(type(x))
# complex
x = 1j
print(type(x))
# list
x = ["피카츄", "라이츄", "파이리"]
# tuple
x = ("피카츄", "라이츄", "파이리")
print(type(x))
# range
x = range(6)
print(type(x))
# dict
x = {"name" : "피카츄", "기술" : "백만 볼트!!!"}
print(type(x))
# set
x = {"피카츄", "라이츄", "파이리"}
print(type(x))
# frozenset
x = frozenset({"피카츄", "라이츄", "파이리"})
print(type(x))
# bool
x = True
print(type(x))
