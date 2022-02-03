import sys

class stakker():  #stakker 클래스
    def __init__(self):  #class 시작
        self.li=[]

    def push(self,n): #push 메소드
        self.li.append(n)
        #stack 뒤에 추가

    def pop(self): #pop 메소드
        if len(self.li)>0:  #리스트 가장 위의 정수를 출력
            print(self.li.pop())
        else: #없으면 -1 출력
            print('-1')
        
    def size(self): #size 크기를 알려줍니다.
        print(len(self.li))
    
    def empty(self): #empty 
        if len(self.li)>0: #비어있지않은경우 0출력
            print('0')
        else:              #빈경우 1출력
            print('1')

    def top(self):         #가장위의정수 출력
        if len(self.li)>0:
            print(self.li[-1])
        else:              #없으면 -1 출력
            print('-1')

stack = stakker()
for i in range(int(sys.stdin.readline())):  #입력된 숫자만큼 반복
    st=sys.stdin.readline().split()  #명령 받기
    if st[0] == "push": #push로 정수를 stack에 넣어준다
        stack.push(int(st[1]))
    elif st[0] == "pop":
        stack.pop()
    elif st[0] == "size":
        stack.size()
    elif st[0] == "empty":
        stack.empty()
    elif st[0] == "top":
        stack.top()