def sPoint(N, M, arr):
    for y, row in enumerate(arr):
        minX = min(row)
        for x in [ix for ix in range(M) if row[ix] == minX]:
            if all(minX >= arr[iy][x] for iy in range(N)):
                print(minX)
                print(y, x)
                return
    print(0)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for y in range(N)]
sPoint(N, M, arr)