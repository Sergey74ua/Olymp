N=int(input())
arrN=list(map(int, input().split()))
arrN.sort()
M=int(input())
arrM=list(map(int, input().split()))
arrM.sort()
K=int(input())
N, M=min(N, K), min(M, K)
arrN=arrN[:N]
arrM=arrM[:M]
posN=[0]*N
L=0
for i in range(K):
    t=arrN[-1]+arrM[-1]
    for j in range(L, N):
        s=arrN[j]+arrM[posN[j]]
        if s<t:
            t=s
            p=j
        #if posN[j]==0:
        #    break
    r=s
    if p>=M:
        L+=1
    else:
        posN[p]+=1
print(r)

# Неполное решение - 36 Превышено максимальное время работы >3.000  0 (1)
#N = int(input())
#arrN = list(map(int, input().split()))
#M = int(input())
#arrM = list(map(int, input().split()))
#K = int(input())
#arr = []
#for i in arrN:
#    for j in arrM:
#        arr.append(i + j) # Может вставка в массив с бинарным поиском позиции
#arr.sort()
#print(arr[K-1])