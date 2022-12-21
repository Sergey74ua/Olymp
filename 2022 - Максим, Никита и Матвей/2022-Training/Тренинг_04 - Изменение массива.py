N=int(input())
arr=list(map(int, input().split()))
temp=0
for i in range(N):
    temp, arr[i] = arr[i], arr[i]-temp
T=int(input())
for i in range(T):
    L, R, V = map(int, input().split())
    arr[L-1]+=V
    if R < N:
        arr[R]-=V
temp=0
for i in range(N):
    arr[i]+=temp
    temp=arr[i]
print(*arr)


#Неполное решение - 18  Превышено максимальное время работы >1.000
#N = int(input())
#arr = list(map(int, input().split()))
#T = int(input())
#for i in range(T):
#    L, R, V = map(int, input().split())
#    for j in range(L-1, R):
#        arr[j] += V
#print(*arr)