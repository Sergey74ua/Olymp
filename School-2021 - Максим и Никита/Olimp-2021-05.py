N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))
K = int(input())

arr = []
for i in arrN:
    for j in arrM:
        arr.append(i + j)
       
arr.sort()

print(arr[K-1])