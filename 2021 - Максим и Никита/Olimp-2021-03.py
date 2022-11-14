N, M=map(int, input().split())
X, Y=map(int, input().split())
X-=1
Y-=1
K=int(input())
arr=dict()
for i in range(K):
    A, B, S=input().split()
    A, B=int(A)-1, int(B)-1
    if A not in arr.keys():
        arr[A]=dict()
    if A in arr.keys() and B not in arr[A]:
        arr[A][B]=[]
    if A in arr.keys() and B in arr[A] and S not in arr[A][B]:
        arr[A][B].append(S)
    if S=='U' and A-1>=0:
        A-=1
        S='D'
    elif S=='L' and B-1>=0:
        B-=1
        S='R'
    elif S=='R' and B+1<M:
        B+=1
        S='L'
    elif S=='D' and A+1<N:
        A+=1
        S='U'
    if A not in arr.keys():
        arr[A]=dict()
    if A in arr.keys() and B not in arr[A]:
        arr[A][B]=[]
    if A in arr.keys() and B in arr[A] and S not in arr[A][B]:
        arr[A][B].append(S)
res='SUCCESS'
for i in input():
    if X in arr.keys() and Y in arr[X].keys() and i in arr[X][Y]:
        res='FAIL'
        break
    if i=='U':
        X-=1
    elif i=='L':
        Y-=1
    elif i=='R':
        Y+=1
    elif i=='D':
        X+=1
    if X<0 or X>=N or Y<0 or Y>=M:
        res='FAIL'
        break
print(res)


# Неполное решение - 34 Превышен лимит по памяти    1.934   0 (1)
#N, M=map(int, input().split())
#X, Y=map(int, input().split())
#X-=1
#Y-=1
#K=int(input())
#arr=[[[] for j in range(M)] for i in range(N)]
#res='SUCCESS'
#for i in range(K):
#    A, B, S=input().split()
#    A, B=int(A)-1, int(B)-1
#    if S not in arr[A][B]:
#        arr[A][B].append(S)
#    if S=='U' and A-1>=0:
#        A-=1
#        S='D'
#    elif S=='L' and B-1>=0:
#        B-=1
#        S='R'
#    elif S=='R' and B+1<M:
#        B+=1
#        S='L'
#    elif S=='D' and A+1<N:
#        A+=1
#        S='U'
#    if S not in arr[A][B]:
#        arr[A][B].append(S)
#for i in input():
#    for j in arr[X][Y]:
#        if i==j:
#            res='FAIL'
#            break
#    if res=='FAIL':
#        break
#    if i=='U':
#        X-=1
#    elif i=='L':
#        Y-=1
#    elif i=='R':
#        Y+=1
#    elif i=='D':
#        X+=1
#    if X<0 or X>=N or Y<0 or Y>=M:
#        res='FAIL'
#        break
#print(res)


# Неполное решение - 34 Превышено максимальное время работы >2.500  0 (1)
#N, M=map(int, input().split())
#X, Y=map(int, input().split())
#K=int(input())
#arr=[]
#res='SUCCESS'
#for i in range(K):
#    A, B, S = input().split()
#    A, B =int(A), int(B)
#    ABS=[A, B, S]
#    if ABS not in arr:
#        arr.append(ABS)
#    if S=='U':
#        ABS=[A-1, B, 'D']
#    elif S=='L':
#        ABS=[A, B-1, 'R']
#    elif S=='R':
#        ABS=[A, B+1, 'L']
#    elif S=='D':
#        ABS=[A+1, B, 'U']
#    if ABS not in arr:
#        arr.append(ABS)
#for i in input():
#    for j in arr: #КАЖЕТСЯ ЭТО ДОЛГО
#        if X==j[0] and Y==j[1] and i==j[2]:
#            res='FAIL'
#            break
#    if res=='FAIL':
#        break
#    if i=='U':
#        X-=1
#    elif i=='L':
#        Y-=1
#    elif i=='R':
#        Y+=1
#    elif i=='D':
#        X+=1
#    if X<1 or X>N or Y<1 or Y>M:
#        res='FAIL'
#        break
#print(res)