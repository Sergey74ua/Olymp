A, B=map(int, input().split())
s=min(A%B, B-A%B)
m=s
for i in range(s):
    Bp=B+i
    Bm=B-i
    ApBp=A%Bp+i
    AmBp=Bp-A%Bp+i
    ApBm=A%Bm+i
    AmBm=Bm-A%Bm+i
    t=min(ApBp, AmBp, ApBm, AmBm)
    if t<m:
        m=t
        if m==0:
            break
print(m)