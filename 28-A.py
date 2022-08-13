A, B=map(int, input().split())
s=min(A%B, B-A%B)
mini=s
for i in range(s):
    for j in range(i):
        if (A+j)%(B+(i-j))==0 or (A+j)%(B-(i-j))==0 or (A-j)%(B+(i-j))==0 or (A-j)%(B-(i-j))==0:
            mini=i
            break
    if mini<s:
        break
print(mini)