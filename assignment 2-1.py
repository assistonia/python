# 업샘플링

N, K = input().split()
N = int(N)
K = int(K)

PictureElement = []

for i in range(N):
    PictureElement.append(input().split())

for i in range(N):
    for p in range(K):
        for j in range(N):
            for k in range(K):
                if (k == K - 1) and ( j == N - 1):
                    print(PictureElement[i][j], "\n" , end="")
                else:
                    print(PictureElement[i][j], "" , end="")