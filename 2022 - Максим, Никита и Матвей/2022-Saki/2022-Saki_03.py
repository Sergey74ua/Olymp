N=int(input())
arr=list(map(int, input().split()))
s=0
for i in range(N):
   s+=(i+1)*arr[i]
r=s
for i in range(N):
   for j in range(i+1, N):
      t=r-((i+1)*arr[i]+(j+1)*arr[j])+((i+1)*arr[j]+(j+1)*arr[i])
      s=max(s, t)
print(s)


#17   Превышено максимальное время работы >2.500
#N = int(input())
#arr = list(map(int, input().split()))
#s=0
#for i in range(N):
#   s+=(i+1)*arr[i]
#for i in range(N):
#   for j in range(i, N):
#      if arr[i] > arr[j]:
#         arr[i], arr[j] = arr[j], arr[i]
#         t = 0
#         for n in range(N):
#            t+=(n+1)*arr[n]
#         s = max(s, t)
#         arr[i], arr[j] = arr[j], arr[i]
#print(s)