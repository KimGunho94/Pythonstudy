'''
파일명: Ex-02-tuple.py

튜플
    단일 변수에 여러 항목을 저장 하는데 사용 된다.
    순서가 있고 병경할 수 없는 List
    둥근 괄호로 작성 된다.
'''

thistuple = ("피카츄", "라이츄", "파이리")
print(thistuple)

# 튜플 길이 len()
thistuple = ("피카츄", "라이츄", "파이리")
print(len(thistuple))

# 항목 가져오기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])

# 튜플값 변경 방법
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
thiscast = list(thistuple)
thiscast[1] = "잠만보"
thistuple = tuple(thiscast)
print(thistuple)

# 튜플 압축 풀기
thistuple = ("피카츄", "라이츄", "파이리", "꼬부기")
(p1, p2, p3, p4) = thistuple

print(type(p1))
print(p1)
print(p2)
print(p3)
print(p4)

# 두개의 튜플 조인
thistuple1 = ("피카츄", "라이츄", "파이리", "꼬부기")
thistuple2 = ("버터풀", "야도란", "피존투", "또가스")

thistuple3 = thistuple1 + thistuple2
print(thistuple3)