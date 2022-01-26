import sys

def hanoi(N, startPoint, endPoint, passPoint, visited): 
  if N == 1: 
    visited.append([startPoint, endPoint])
    return
  
  hanoi(N-1, startPoint, passPoint, endPoint, visited)
  visited.append([startPoint, endPoint])
  hanoi(N-1, passPoint, endPoint, startPoint, visited)

if __name__ == '__main__':
  N = int(sys.stdin.readline())
  visited = []
  hanoi(N, 1, 3, 2, visited)
  
  print(len(visited))
  for start, end in visited:
    print(f"{start} {end}")