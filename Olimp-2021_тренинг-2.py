T = int(input())
for i in range(T):
    N = int(input())
    if N == round(N**(1.0/3.0))**3:
        print('YES')
    else:
        print('NO')
