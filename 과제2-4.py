import math
class calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def add(self):
       return self.x + self.y
   
    def sub(self):
           return self.x - self.y

    def mul(self):
           return self.x * self.y

    def div(self):
        if self.y == 0:
            print("0은 불가능합니다")
        else:
           return self.x / self.y

class improved_calculator(calculator):
    
    def pow(self):
        return math.pow(self.x,self.y)
    
    def gcd(self):
        return math.gcd(self.x,self.y)
    
def c():
    while True:
        print("""
아래에 사용을 원하시는 사칙연산을 선택해주세요!
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 제곱
6. 최대 공약수
7. 종료""")
        m = int(input(">> "))
        
        if m == 7:
            print("계산기 프로그램을 종료합니다")
            break
        else:
            x, y = map(int,input("숫자를 입력해주세요: ").split())
            if m == 1:
                print(calculator(x,y).add())
            if m == 2:
                print(calculator(x,y).sub())
            if m == 3:
                print(calculator(x,y).mul())
            if m == 4:
                print(calculator(x,y).div())
            if m == 5:
                print(improved_calculator(x,y).pow())
            if m == 6:
                print(improved_calculator(x,y).gcd())
                
c()