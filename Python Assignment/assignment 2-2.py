# 하노이 탑

# 원반 이동 출력 함수
def print_move(start, end):
    print(start, end)

# 하노이 탑 알고리즘 함수
def hanoi_tower(N, start, end, middle):

    if N == 1:
        print_move(start, end)
        return 
    
    hanoi_tower(N - 1, start, middle, end)
    print_move(start, end)
    hanoi_tower(N - 1, middle, end, start)
    return 



n = int(input())
final_count = 1

for i in range(n):
    final_count *= 2

print(final_count - 1)
hanoi_tower(n, 1, 3, 2)