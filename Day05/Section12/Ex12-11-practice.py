'''
파일명: Ex12-11-practice.py
'''
import random
import time

pot = [n for n in range(1, 46)]  # for 문을 사용 하여 n에 값을 넣어 준다
jackpot = []

for n in range(1, 7):  # for 문을 사용 하여 n에 값을 입력 한다
    random.shuffle(pot)
    pick = pot.pop()  # 한번 나온 값을 .pop()로 지워 준다
    print('{}번째 당첨 번호는 {}입니다.'.format(n, pick))
    jackpot.append(pick)
    time.sleep(2)

jackpot.sort()
print('이번 당첨번호는 {} 입니다.'.format(jackpot))
