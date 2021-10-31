N = int(input())
S = 0

if n < 2:
    print(0)

elif n == 2:
    print(1)

else:
    for i in range(3, N//2, 2):
        while i <= n ** .5:
            if n % i == 0:
                S += 1
                break
            i += 1
    print(S)