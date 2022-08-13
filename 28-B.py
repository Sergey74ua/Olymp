T = int(input())
for i in range(T):
    n, A = map(int, input().split())
    R = 0
    if len(str(A)) >= n-1:
        for j in str(int(''.join(['1']*n))*A):
            R += int(j)
    else:
        for j in str(int(''.join(['1']*len(str(A))))*A):
            R += int(j)
        s = int(''.join(['1']*(len(str(A))+2)))*A
        R += (int(n)-len(str(A)))*int(str(s)[len(str(s))//2])
    print(R)