from math import *

# 새로운 오류 문구
class Finish(Exception):
    def __init__(self, CustomError):
        self.custom_error = CustomError
    
    def __str__(self):
        return self.CustomError

try:
    class calculator:
        
        def __init__(self, input1, input2, mode):
            self.input1 = input1
            self.input2 = input2
            self.mode = mode
                

            
    class improved_calculator(calculator):

        def get_output(self):
            if self.mode == 1:
                result = self.input1 + self.input2

            if self.mode == 2:
                result = self.input1 - self.input2
                
            if self.mode == 3:
                result = self.input1 * self.input2

            if self.mode == 4:
                if self.input2 != 0:
                    result = self.input1 / self.input2
                else:
                    print("0으로 나눌 수 없습니다.")
                    return

            if self.mode == 5:
                result = pow(self.input1, self.input2)

            if self.mode == 6:
                result = gcd(self.input1, self.input2)
                

            return result



    def main():
        result = 0
        print("""\
아래에 사용을 원하시는 사칙연산을 선택해주세요!
1. 더하기
2. 빼기
3. 곱하기
4. 나누기
5. 제곱
6. 최대 공약수
7. 종료\
        """)
        mode = int(input(">> "))
        if mode == 7:
            raise Finish("계산기 프로그램을 종료합니다.")
        a, b = input("두 숫자를 입력해주세요: ").split()
        a, b = int(a), int(b)
        EndResult = improved_calculator(a, b, mode)


        print(EndResult.get_output())


    while True:
        main()


except Finish as exception:
    print("계산기 프로그램을 종료합니다.")

    