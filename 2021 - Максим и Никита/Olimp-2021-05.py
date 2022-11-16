N=int(input())
arrN=list(map(int, input().split()))
arrN.sort()
M=int(input())
arrM=list(map(int, input().split()))
arrM.sort()
K=int(input())
n=m=0
print()
print(arrN)
print(arrM)
print()
while n+m<K:
    s=arrN[n]+arrM[m]
    print(n, m, ' - ', arrN[n], arrM[m], ' - ', s) # ПРОПУСКИ, не каждое с каждым суммируется.
    if arrN[n+1]+arrM[m]<=arrN[n]+arrM[m+1]:
        n+=1
    else:
        m+=1
print(s)


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