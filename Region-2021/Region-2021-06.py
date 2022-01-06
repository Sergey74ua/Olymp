x = input()
k = input()

if k == '0':
    for i in x:
        if i == x[0]:
            continue
        elif i < x[0]:
            break
        else:
            x[0] = str(int(x[0]) + 1)
            break
    k = ''
    for i in x:
        k = k + x[0]
else:
    while True:
        if max(x.count(x[0]), x.count(x[-1])) >= len(x) - 1:
            break
        else:
            x = str(int(x)+1)
    k = x

print(k)
