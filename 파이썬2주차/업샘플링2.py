
A=int(input('가로세로의 크기를 입력해주세요>>')) 
B=int(input('배수를 입력해주세요>>'))
#가로세로와 크기를 입력 받습니다.
picture=[list(map(int, input("그림정보를 입력해주세요: ").split())) for _ in range(A)]
#그림 픽셀정보입력 받기


#그림 출력
for a in range(A): #A만큼 반복
    for q in range(B): #B만큼 반복
        for b in range(A):
            for w in range(B):
                print(picture[a][b], end = ' ')
        print()