# 반복문 이용해서 구구단 출력하기

while 1:
    print("-" * 63)
    print("""\
\"구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료\
    """)
    print("-" * 63)
    mode = int(input("숫자를 입력하세요: ")) #정수 형태로 숫자를 변환



    # 홀수 구구단
    if mode == 1:
        for i in range(3, 9 + 1, 2):
            print(str(i) +"단")
            for j in range(1, 9 + 1):
                print(i, "*", j, "=", i*j)



    # 짝수 구구단
    elif mode == 2:
        for i in range(2, 9 + 1, 2):
            print(str(i) +"단")
            for j in range(1, 9 + 1):
                print(i, "*", j, "=", i*j)



    # 종료
    elif mode == 3:
        break




    # 잘못된 입력
    else:
        print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")

print("프로그램을 종료합니다.")