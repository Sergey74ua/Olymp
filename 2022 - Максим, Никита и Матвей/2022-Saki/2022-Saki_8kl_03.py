N=int(input())
arr=[]
d=100
for i in range(N):
    s=input()
    arr.append(s)
    d=min(d, len(s))
for i in range(d):
    t=arr[0][i]
    for j in range(N):
        if arr[j][i]!=t:
            d-=1
            break
print(d)