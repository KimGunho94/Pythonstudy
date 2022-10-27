'''
파일명: Ex12-1-module.py

모듈(module)
    언제든지 변수나 함수 또는
    클래스를 모아 놓은 파일을 모듈이라고 한다.
    한 마디로 파이썬 파일(.py) 이다.

모듈 사용법
import 무듈명

'''

import converter

miles = converter.kilometer_to_miles(150)
print('150km={}miles'.format(miles))

pounds = converter.gram_to_pounds(90000)
print('90000g={}pounds'.format(pounds))

