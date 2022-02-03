import math
import os
import random
import re 
import sys

def miniMaxSum(arr):
    Min=sum(arr)-max(arr)
    #arr 에서 다 합친것에 최대값을 뺀다.
    Max=sum(arr)-min(arr)
    #arr 에서 다 합친것들 중에 최소값을 뺀다. 
    print(Min , Max)
    #위에서 구한 것들을 출력

    
if __name__ == '__main__':
    arr=list(map(int,input().rstrip().split())) 
    #입력을 받고 , rstrip 공백을 제거, split  일정한 규칙으로 잘라준다

    miniMaxSum(arr)