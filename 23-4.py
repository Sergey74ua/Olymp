arr = list(input().split())
arr.sort()
s = ''.join(arr)

for i in range(317, 1000):
    q = i * i
    test = list(str(q))
    test.sort()
    r = ''.join(test)
    if s == r:
        print(q)
        break