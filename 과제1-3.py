new_id=input("새로운 아이디를 작성해주세요.")

# 1단계
id = new_id.lower()

# 2단계
delete = "~!@#$%^&*()+`=[]}{:;?/<>,"
for i in range(len(delete)):
        id = id.replace(delete[i],"")

#3단계
for i in range(len("..")):
    id = id.replace("..",".")

#4단계
id = id.strip(".")

#5단계
if id=='':
    id=id.replace('','a')

#6단계
if len(id) > 15:
    id = id[:15]
    if id[-1] == ".":
        id = id[:-1]

#7단계
else:
    if id[-1]==".":
        id=id.replace(id[-1],"")


while len(id)<3:
        id = id + id[-1]
       
#종료
print("ID : {}".format(id))