N=int(input())
arrN=list(map(int, input().split()))
M=int(input())
arrM=list(map(int, input().split()))
K=int(input())

sumN=sumM=0
countN=countM=0
minN=minM=0
lostN=lostM=-1

while sumN*sumM<=K: #Выбирает меньшие значения, а не меньшую сумму
    if countN==0:
        minN=int(1e9)+1
        for j in range(N):
            if lostN<arrN[j]<minN:
                minN=arrN[j]
                countN=1
            elif arrN[j]==minN:
                countN+=1
    if countM==0:
        minM=int(1e9)+1
        for j in range(M):
            if lostM<arrM[j]<minM:
                minM=arrM[j]
                countM=1
            elif arrM[j]==minM:
                countM+=1
    if minN<=minM:
        lostN=minN
        sumN+=countN
        countN=0
    else:
        lostM=minM
        sumM+=countM
        countM=0
    print(minN, minM, minN+minM)
print(minN+minM)

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