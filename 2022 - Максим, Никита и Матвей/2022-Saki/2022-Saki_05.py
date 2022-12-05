import math

N = int(input())
arr = list(map(int, input().split()))
tmp = [[0 for j in range(N)] for i in range(N)]

s=0
res=[]

for i in range(N):
    for j in range(i+1, N):
        tmp[i][j] = math.gcd(arr[i], arr[j])

for i in range(N):
    if sum(tmp[i])>1:
        s+=1
        res.append(arr[i])

#требуется сортировка [res]

print(s)
print(*res)