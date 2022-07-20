T = int(input())
for i in range(T):
  mini = 100
  maxi = 0
  N = int(input())
  arr = list(map(int, input().split()))
  for i in range(N):
    mini = min(mini, arr[i])
    maxi = max(maxi, arr[i])
  print((maxi-mini)*2)
