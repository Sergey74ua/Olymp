N=int(input())
arr=list(map(int, input().split()))
s=m=sum(arr)
r=0
for i in arr:
    r+=i
    s-=i
    m=min(m, abs(s-r))
print(m)