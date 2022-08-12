T = int(input())
for i in range(T):
    n, A = map(int, input().split())
    R = 0
    if len(str(A)) >= n:
        for j in str(int(''.join(['1']*n))*A):
            R += int(j)
    else: ####################################
        s = int(''.join(['1']*len(str(A))))*A
        for j in str(s):
            R += int(j)
        R += (n-len(str(A))*int(s[int(len(s)/2)]))
    print(R)