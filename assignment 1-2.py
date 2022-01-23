# 책정보 출력 프로그램

book_info = {
    "HarryPotter1" : [[1997], [6], [26]],
    "TheLoadOfTheRings" : [[1954], [7], [29]],
    "engineering_mathematics" : [[2018], [2], [28]]
}

while 1:
    BookTitle = input("원하시는 책을 입력하세요.\n> ")


    if (BookTitle == "HarryPotter1") or\
    (BookTitle == "TheLoadOfTheRings") or\
    (BookTitle == "engineering_mathematics"):
        print("*" * 37)
        print("""\
원하시는 정보를 선택해주세요.
1. 년
2. 월
3. 일
4. 종료\
        """)
        print("*" * 37)

        mode = int(input()) #입력값을 정수 형태로 변환


        # 책 정보와 일치하는 경우
        if mode == 1:
            print(str(book_info[BookTitle][0][0]) + "년입니다.")

        elif mode == 2:
            print(str(book_info[BookTitle][1][0]) + "월입니다.")
        
        elif mode == 3:
            print(str(book_info[BookTitle][1][0]) + "일입니다.")
        
        elif mode == 4:
            break
        
    # 책 정보와 일치하지 않은 경우
    else:
        print("제목을 다시 입력해주세요.")

print("프로그램이 종료되었습니다.")



