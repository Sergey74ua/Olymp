n = int(input())
arr = list(map(int, input().split()))
s = 0
res = []
q = int(input())
for i in range(q):
    line = list(map(int, input().split()))
    if line[0] == 1:
        arr[(line[1] + s - 1) % n] = line[2]
    else:
        s = (s - line[1]) % n
        #temp = [0] * n
        #for j in range(n):
        #    temp[j] = arr[(j - line[1]) % n]
        #arr = temp
    res.append(sum(arr))
for i in res:
    print(i)