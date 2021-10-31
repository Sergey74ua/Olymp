T = int(input())

arr = []
for i in range(T):
    N = int(input())
    X = N ** (1.0/3.0)
    
    if N == round(X) ** 3:
        arr.append('YES')
    else:
        arr.append('NO')

for i in arr:
    print(i)
