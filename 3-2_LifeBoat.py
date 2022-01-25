N=int(input("인원을 입력 하세요: "))
limit=int(input("구명보트의 무게 제한을 입력하세요.(40~240): "))
print("{}명의 몸무게를 입력 하세요:".format(N))
people=[]
for i in range(N):
    people.append(input())
people.sort()
i=0
j=1
boat=0
while 1:
    value=int(people[i])+int(people[N-j])
    if value <= limit :
        i+=1
        j+=1
        boat+=1
    elif value> limit :
        j+=1
        boat+=1
    if i>(N-j ):
        break
    elif i==(N-j ):
        boat+=1
        break
print(boat)


