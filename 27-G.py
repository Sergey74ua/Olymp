T=int(input())
for t in range(T):
    N=int(input())
    s=list(map(int, input().split()))
    arr=[]
    for i in range(N):
        x=s[2*i]*10000+s[2*i+1]
        arr.append(x)
    arr.sort()
    r=1
    for i in range(N-1):
        if arr[i]>arr[i+1]:
            r=+1
    print(r)


#2  Превышено максимальное время работы >1.000
#T=int(input())
#for t in range(T):
#    N=int(input())
#    arr=list(map(int, input().split()))
#    arrW=[]
#    arrH=[]
#    for i in range(0, N*2, 2):
#        arrW.append(arr[i])
#        arrH.append(arr[i+1])
#    for i in range(N):
#        for j in range(i+1, N):
#            if arrW[i]>arrW[j]:
#                arrW[i], arrW[j]=arrW[j], arrW[i]
#                arrH[i], arrH[j]=arrH[j], arrH[i]
#            elif arrW[i]==arrW[j]:
#                if arrH[i]>arrH[j]:
#                    arrW[i], arrW[j]=arrW[j], arrW[i]
#                    arrH[i], arrH[j]=arrH[j], arrH[i]
#    s=1
#    for i in range(N-1):
#        if arrW[i]>=arrW[i+1] or arrH[i]>=arrH[i+1]:
#            s+=1
#    print(s)