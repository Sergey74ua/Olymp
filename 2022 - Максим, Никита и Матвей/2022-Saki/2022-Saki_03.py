N = int(input())
arr = list(map(int, input().split()))
s=0

for i in range(N):
   s+=(i+1)*arr[i]

print(s)