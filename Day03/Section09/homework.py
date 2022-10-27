''' 숙제 '''
id = None
pwd = None
# 아이디 입력
while True:
    id = input('아이디를 입력 하세요 (3글자 이상) >>> ')
    if len(id) >= 3:
        break
    print('> 3글자 이상 입력 해주세요.')
# 패쓰워드 입력
while True: # 반복 실행문
    pwd = input('패쓰워드를 입력 하세요 (영문, 숫자 포함 8글자 이상) >>> ')
    isContainAlpha = False # 영문이 있을 떄
    isContainNumeric = False # 숫자가 있을 때

    for ch in pwd:
        if ch.isalpha():
            isContainAlpha = True # 영문이 없을 때
        elif ch.isnumeric():
            isContainNumeric = True # 숫자가 없을 때

    if not isContainAlpha or not isContainNumeric or len(pwd) < 8: # 영문 이나 숫자가 8글자 미안일 때 실행 하도록 하는 조건
        print('영문, 숫자 포함 8글자 이상 입력해 주세요.')
        continue # 다시 페스워드 입력으로 넘어가게 한다.

    pwdChk = input('패쓰워드를 한번 더 입력하세요 >>> ')
    if pwd != pwdChk:
        print('> 일치하지 않습니다. 다시 입력해주세요.')
        continue
    break
print('회원가입 완료!')

# 로그인
while True:
    loginId = input('아이디를 입력하세요 >>> ')
    if id == loginId:
        break
    print('아이디가 일치하지 않습니다. 다시 입력해주세요.')
    continue

while True:
    loginPwd = input('패쓰워드를 입력하세요 >>>')
    if pwd == loginPwd:
        break
    print('> 패쓰워드가 일치하지 않습니다.')

print('로그인 완료!')

