'''
파일명: Ex02-8-dict.py

Dictionary
    key:value 로 이루어져 쌍으로 데이터 값을 저장 하는데 사용
    키값 중복 불가.
'''

thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict)

'''
키 이름을 사용하여 참조 할 수 있다.
'''
# 값 가져오기
thisdict = {
    "brand" : "구찌",
    "model" : "g001",
    "year" : 2022
}
print(thisdict["brand"])
print(thisdict.get("model")) # .get 함수로 가져올수 있다.

# 키 목록 가져오기
print(thisdict.keys())

# 추가 하기
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"bgcolor" : "black"})
print(thisdict)

# 변경 하기
thisdict["color"] = "yellow"
thisdict.update({"bgcolor" : "blue"})
print(thisdict)

# 제거 하기
thisdict.pop("model")
print(thisdict)

# 마지막 삽입된 항목 제거하기
thisdict.popitem()
print(thisdict)