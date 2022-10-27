'''
파일명: Ex14-6-jsonWriter.py
'''
'''
# 첫 번째 실행
import json

dict_list = [
    {
        'name': 'james',
        'age': 20,
        'spec': [
            175.5,
            70.5

        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    },
]

json_string = json.dumps(dict_list)

with open('dictlist.json', 'w') as file:
    file.write(json_string)

print('dictList.json 파일이 생성되었습니다.')
'''
# 두 번째 실행
import json

dict_list = [
    {
        'name': 'james',
        'age': 20,
        'spec': [
            175.5,
            70.5

        ]
    },
    {
        'name': 'alice',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    },
{
        'name': '홍길동',
        'age': 21,
        'spec': [
            168.5,
            60.5
        ]
    }
]
json_string = json.dumps(dict_list, indent=4, ensure_ascii=False)  # ensure_ascii=False 추가하면 한글로 직역해준다.
print(json_string)

with open('dictlist.json', 'w') as file:
    file.write(json_string)

print('dictList.json 파일이 생성되었습니다.')
