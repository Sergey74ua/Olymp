
x = input()
k = input()

if k == '0':
    n = x[0]
    for i in x:
        if i == n:
            continue
        elif i < n:
            break
        else:
            n = str(int(n) + 1)
            break
    k = ''
    for i in x:
        k = k + n
else:
    while True:
        if max(x.count(x[0]), x.count(x[-1])) >= len(x) - 1:
            break
        else:
            x = str(int(x)+1)
    k = x

print(k)