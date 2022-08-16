T = int(input())
for i in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  arr.sort(reverse=True)
  s = 0
  for k in range(N//3):
    s+=arr[k*3+2]
  print(s)