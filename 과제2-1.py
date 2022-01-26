import sys

def upSampling(K, pixel):
  newPixel = []

  for row in pixel:
    newRow = []
    for bit in row:
      for _ in range(K):
        newRow.append(bit)
    for _ in range(K):
      newPixel.append(newRow)
  
  for row in newPixel:
    print(' '.join(map(str, row)))

N, K = map(int, sys.stdin.readline().split())
pixel = []
for _ in range(N):
  row = list(map(int, sys.stdin.readline().split()))
  pixel.append(row)

upSampling(K, pixel)