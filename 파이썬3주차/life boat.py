people=[]  #배열 초기화
limit=0    #변수 초기화

def Boatmove(people, limit): #메소드 설정
    people.sort() #정렬
    boatmovetimes=0  #횟수 변수
    i=0
    j=len(people)-1 #i j 끝과 끝 두명을 더해준다
    while i<j: 
        boatmovetimes+=1
        if people[j]+people[i]<=limit: #끝과 끝을 하나씩 더해본다.(2명분)
            i+=1
        j-=1
    return boatmovetimes

print('인원을 입력하세요.')
n=int(input('>>'))  #n개만큼의 입력
print('구명보트의 무게 제한을 입력하세요.(40~240)')
limit=int(input('>>'))
print(n,'명의 몸무게를 입력하세요.')
for p in range(n):  #n명만큼의 사람의 몸무게를 입력 받는다.
    people.append(int(input()))

print(Boatmove(people,limit)) #결과를 출력 한다.