for i in range(int(input())):
    L, R = map(int, input().split())
    print(((R+R%2)**2-(L-L%2)**2)//4)

#T=int(input())
#for i in range(T):
#    L, R = map(int, input().split())
#    if L%2==0:
#        L+=1
#    if R%2==0:
#        R-=1
#    print(((R-L)//2+1)*(L+R)//2)

#Неполное решение - 14  Превышено максимальное время работы >1.000
#T=int(input())
#for i in range(T):
#    L, R = map(int, input().split())
#   if L%2==0:
#        L+=1
#   if R%2==0:
#        R-=1
#   s=0
#   for j in range(L, R+1, 2):
#       s+=j
#   print(s)