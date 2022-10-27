'''
파일명: Ex11-2-variable-local-global.py
지역변수(local)
    함수 내부 선언
    함수 내부에서만 사용가능
전역변수(global)
    함수 외부 선언
    함수 내부 외부 모두 사용가능
'''

gVar = '전역'
def globalAndlocal():
    lvar = '지역'
    print(gVar, '변수 입니다.')  # 전역 변수 참조만 하고있다.
    print(lvar, '변수 입니다.')

globalAndlocal()


gVar = '전역'
def globalAndlocal():
    lvar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'  # 전역함수가 안에 있으면 지역 함수로 변경된다.
    print(gVar, '변수 입니다.')
    print(lvar, '변수 입니다.')

globalAndlocal()
print()
# 전역변수 선언

total = 0

def gift(dic, who, money):
    global total  # 전역변수 total을 사용한다.
    total += money
    dic[who] = money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 6)
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))

