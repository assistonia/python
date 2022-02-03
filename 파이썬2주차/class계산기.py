import math

class calculator:
    def __init__(self,first,second): #시작할때 init 로 시작 정의
        self.first=first
        self.second=second
    def add(self):  #덧셈
        ans=self.first+self.second
        return ans
    def minus(self): #뺄셈
        ans=self.first-self.second
        return ans
    def multi(self): #곱셈
        ans=self.first*self.second
        return ans
    def div(self): #나눗셈
        if self.second==0:  #예외 처리
            return "0으로는 나눌 수 없습니다."
        else:
            ans=self.first/self.second
        return ans

class improved_calculaltor(calculator):
    def square(sample):
        return math.pow(sample.first,sample.second)
    def common(sample):
        return math.gcd(sample.first,sample.second)

def menu():
    print('아래에 사용을 원하시는 사칙연산을 선택해주세요!')
    print('1.더하기')
    print('2.빼기')
    print('3.곱하기')
    print('4.나누기')
    print('5.제곱')
    print('6.최대 공약수')
    print('7.종료')

def main():
    while 1: #메뉴
        menu()
        menuselect=input('>>') 

        if menuselect=='7':  #7일경우 종료
            print("프로그램을 종료합니다.")
            break

        q,w =map(int, input("두 수를 입력해 주세요: ").split())

        s=improved_calculaltor(q,w)

        if menuselect =='1':
            print(s.add())
            print()
        if menuselect =='2':
            print(s.minus())
            print()
        if menuselect =='3':
            print(s.multi())
            print()
        if menuselect =='4':
            print(s.div())
            print()
        if menuselect =='5':
            print(s.square())
            print()
        if menuselect =='6':
            print(s.common())
            print()

main()