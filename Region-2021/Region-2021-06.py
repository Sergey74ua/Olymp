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
    for i in x:
        pass

print(k)