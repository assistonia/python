while True:
    print("""\
          --------------------------------------------------
          "구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.
          1. 홀수 구구단
          2. 짝수 구구단
          3. 종료
          --------------------------------------------------
          \
          """);
    
    i=int(input("숫자를 입력하세요: "))
    
    while i==1:
        for x in range(3,10,2):
            print("{}단".format(x))
            for y in range(1,10):
                print("{} * {} = {}".format(x,y,x*y));
        if x==9:
            break
        
    while i==2:
        for x in range(2,10,2):
            print("{}단".format(x))
            for y in range(1,10):
                print("{} * {} = {}".format(x,y,x*y));
        if x==8:
            break
        
    while 3<i or i<0:
        print("잘못입력하셨습니다. 1~3번 숫자를 입력하세요.")
        break
    
    if i==3:
        print("프로그램을 종료합니다.")
        break