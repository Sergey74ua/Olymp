N, M=map(int, input().split())
arr=[]
st=r=0
for i in range(N):
    row=list(map(int, input().split()))
    arr.append(row)
    m=1e10
    for x in range(M):
        m=min(m, row[x])
    if m>st:
        st,y=m,i
for x in range(M):
    if st==arr[y][x]:
        for i in range(N):
            if st<arr[i][x]:
                break
            if i==N-1:
                r=str(st)+'\n'+str(y)+' '+str(x)
                break
print(r)