def hanoi(a,A,B,C):
    # 1개일때 A에서 C로
    if a==1:
        print (A,C)
        return
    # n-1개를 A에서 B로
    hanoi(a-1,A,C,B)
    #가장 큰 원반을 A에서 C로
    print(A,C)
    #원반 n-1개를 B에서 C로 이동
    hanoi(a-1,B,A,C)

disk=int(input("원반 갯수를 입력해주세요>>"))
print(2**disk-1)
hanoi(disk,1,2,3)