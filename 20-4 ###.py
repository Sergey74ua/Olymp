arr = []
N = int(input())
L = (N - 1) * 4
for i in range((N - 1) // 2):
    arr.append([])
    for j in range(L):
        arr[i].append(j + 1)
    L -= 8

T = int(input())
for i in range(T):
    K, S = map(int, input().split())
    L = len(arr[K - 1])
    for j in range(L):
        arr[K - 1][j] = (arr[K - 1][j] - S - 1) % L + 1

arrQ = [[0] * N] * N

#переброска из одного массива в другой (4 хода)

for i in arrQ:
    print(*i)