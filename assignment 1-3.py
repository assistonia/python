# 조건에 맞는 신규 아이디 추천 프로그램

new_id = input()
special_char="~!@#$%^&*()=+[{]}:?,<>/"
OverlappedPeriod='..'


# 대문자를 소문자로 치환
new_id = new_id.lower() 


# 특정 특수문자 제거
for i in special_char:
    if i in new_id:
        new_id = new_id.replace(i,"")


# 반복되는 마침표(.) 하나로 통일
while 1:
    for i in OverlappedPeriod:
        if i in new_id:
            new_id = new_id.replace("..","&")

    if "&" not in new_id:
        break

    new_id = new_id.replace("&",".")


# 마침표가 처음이나 끝에 있으면 제거
new_id = new_id.strip(".")


# 빈 문자열인 경우 a 출력
if len(new_id) == 0:
    new_id = 'aaa'


# 문자열을 리스트로 치환하기
new_id = list(new_id)
    

# 문자열의 길이가 15자 초과인 경우 제한하기
if len(new_id) > 15:
    del new_id[15:]


# 문자열의 길이가 2자 이하이면, 마지막 문자 반복
if len(new_id) == 1:
    new_id *= 3

if len(new_id) == 2:
    new_id.append(new_id[1])


# 리스트를 문자열로 환원하기
new_id = "".join(new_id)


# 마침표가 처음이나 끝에 있으면 제거(15번째 문자가 마침표인 경우)
new_id = new_id.strip(".")


print(new_id)