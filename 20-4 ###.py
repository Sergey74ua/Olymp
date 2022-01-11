N = int(input())
arr = [0] * ((N - 1) // 2)
T = int(input())
for i in range(T):
    K, S = map(int, input().split())
    arr[K-1] = (arr[K-1] + S) % ((N - 1) * 4 - (K - 1) * 8)

matrix = [[1] * N] * N

for i in range(len(arr)):
    tN = N - i * 2
    L = (tN - 1) * 4
    for x in range(tN - 1):
        matrix[i][(N - tN) // 2 + x] = 88 #(x - arr[i]) % L ПРОБЛЕМА С Х т.е. с    N - tN + x
    #    matrix[N - i][N - tN + x] = (L - x - arr[i]) % L
    #for y in range(tN - 1):
    #    matrix[y][i] = (L - y * (tN - 2) - arr[i]) % L
    #    matrix[y][tN - i] = (y * (tN - 2) - arr[i]) % L

for i in matrix:
    print(*i)