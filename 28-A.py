A, B=map(int, input().split())
s=min(A%B, B-A%B)
for i in range(s):
    Bp=B+i
    Bm=B-i
    s=min(s, A%Bp+i, Bp-A%Bp+i, A%Bm+i, Bm-A%Bm+i)
print(s)