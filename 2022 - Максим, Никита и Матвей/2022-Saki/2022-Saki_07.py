N, M=map(int, input().split())
r=0
for i in range(N, M+1):
    s=str(i)
    if len(s)==1:
        r+=1
        continue
    t=0
    for j in range(len(s)-1):
        if abs(int(s[j])-int(s[j+1]))==1:
            t+=1
        else:
            break
    if t==len(s)-1:
        r+=1
print(r)