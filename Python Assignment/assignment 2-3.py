import imp
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    FullSum = 0

    for i in range(5):
        FullSum += arr[i]

    for i in range(5):
        for j in range(5):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(FullSum - arr[0], FullSum - arr[4])


# 직접 모듈(함수)를 실행한 경우, 출력 예시
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)