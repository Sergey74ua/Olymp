N, M=map(int, input().split())
arr=[]
fin=[[N-1, M-1]]
for y in range(N):
    arr.append(list(map(int, input().split())))
    for x in range(M):
        if arr[y][x]==0:
            fin.append([y, x])
way=[[int(1e6)+1 for j in range(M)] for i in range(N)]
way[0][0]=0

for i in arr:

print()