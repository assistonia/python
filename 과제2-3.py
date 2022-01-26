def miniMaxSum(arr):
      # Write your coode here
  maximum = 0
  minimum = 0
  arr.sort()

  for i in range(len(arr)-1):
    minimum += arr[i]

  for i in range(1, len(arr)):
    maximum += arr[i]

  print(f"{minimum} {maximum}")

if __name__ == '__main__':
  arr = list(map(int, input().rstrip().split()))
  
  miniMaxSum(arr)