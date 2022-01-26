book_info = {
    "Harrypotter1" : [[1997],[6],[26]],
    "TheLordOfTheRings" : [[1954],[7],[29]],
    "engineering_mathmatics1" : [[2018],[2],[28]]
}

while True:
    name=input("원하시는 책을 입력하세요 \n")
    
    if name in book_info:
        print("""

        ---------------------------
        원하시는 정보를 선택해주세요.
        1. 년
        2. 월
        3. 일
        4. 종료
        ---------------------------
   """)
        x=int(input())
        
        while x==1:
            print("{}년 입니다.".format(book_info[name][0][0],))
            break
        while x==2:
            print("{}월 입니다.".format(book_info[name][1][0],))
            break
        while x==3:
            print("{}일 입니다.".format(book_info[name][2][0],))
            break
        while 4<x or x<0:
            print("제목을 다시 입력해주세요.")
            break
        while x==4:
            print("프로그램이 종료되었습니다.")
            break
    break