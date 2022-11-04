N, M = map(int, input().split())
arr = []

for y in range(N):
    arr.append(list(map(int, input().split())))

arrFinish = [[N-1, M-1]]
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            arrFinish.append([y, x])

S = arr[0][0] + arr[N-1][M-1]
for i in arrFinish:
    # нахождение кратчайшей суммы до точки S
    pass


print(S)