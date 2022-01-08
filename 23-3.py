N = int(input())
L = -(10 ** 9)
R = 10 ** 9

for i in range(N):
    P, Z = input().split()
    P = int(P)
    if Z == '>' and P < R:
        R = P
    if Z == '<' and P > L:
        L = P

print(abs(R - L))