'''
파일명 : Ex08-2-continue.py

continue
    while 문이나 for 문과 같은 반복문을 강제로 건너뛰기(아래코드를 실행하지 않는다.)
'''
total = 0
for a in range(1, 101):
    if a % 3 == 0: # a % 3 == 0 3의 배수를 의미한다.
        continue
    print('a : {}, total {}'.format(a, total))
    total += a
print(total)

