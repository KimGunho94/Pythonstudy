'''
[회원가입]
아이디를 입력하세요 (3글자 이상) >>>
> 3글자 이상 입력해 주세요.

아이디를 입력하세요 (3글자 이상) >>>

패쓰워드를 입력하세요(영문 숫자 포함 8자 이상) >>>
>영문 숫자 포함 8자 이상 입력해주세요

패쓰워드를 한번 더 입력하세요 >>>
>일치하지 않습니다. 다시 입력해 주세요.

패쓰워드를 입력하세요 (영문 숫자 포함 8자이상) >>>

패쓰워드를 한번 더 입력하세요 >>>

회원가입 완료!!

[로그인]
아이디를 입력하세요 >>>
>아이디가 일치하지 않습니다.

패쓰워드를 입력하세요 >>>
> 패쓰워드가 일치하지 않습니다.

로그인 완료
'''
id = None
pwd = None
while True:
    id = input('아이디를 입력해주세요.(3글자 이상) >>> ')
    if len(id) >= 3:
        break
    print('> 글자 이상 다시 입력해주세요')
    continue

while True:
    pwd = input('비밀번호를 입력해주세요.(영문, 숫자 포함 8글자 이상) >>> ')
    isContainAlpha = False
    isContainNumeric = False

    for ch in pwd:
       if ch.isalpha():
           isContainAlpha = True
       elif ch.isnumeric():
           isContainNumeric = True

    if not isContainAlpha or not isContainNumeric or len(pwd) < 8:
        print('영문, 숫자 포함 8자 이상 입력해주세요.')
        continue
    pwdChk = input('비밀번호를 한번 더 입력해주세요.')
    if pwd != pwdChk:
        print('일치하지 않습니다. 다시 입력해주세요')
        continue
    break
print('회원가입 완료!!')

while True:
    loginId = input('아이디를 입력해주세요.')
    if id == loginId:
        break
    print('일치하지 않습니다. 다시 입력해주세요.')
    continue

while True:
    loginPwd = input('비밀번호를 입력해주세요.')
    if pwd == loginPwd:
        break
    print('비밀번호가 일치하지 않습니다. 다시 입력해주세요.')
    continue

print('로그인 완료!!')





