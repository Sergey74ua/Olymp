T = int(input())

for i in range(T):
    L, R = map(int, input().split())
    
    if L % 2 == 0:
        L += 1
    if R % 2 == 0:
        R -= 1
    
    print((R + L) // 2 * ((R - L) // 2 + 1))