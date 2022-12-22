import math
N=int(input())
r=1
for i in range(2, int((N)**0.5)+1):
  s=round(math.log(N, i))
  if i**s==N:
    r=s
    break
print(r)

#57 Превышено максимальное время работы >2.000  0 (1)
#import math
#N=int(input())
#r=1
#for i in range(2, int((N)**0.5)+1):
#  s=round(math.log(N, i))
#  if i**s==N:
#    r=s
#    break
#print(r)

#48 Превышено максимальное время работы >2.000  0 (1)
#N=int(input())
#r=1
#for i in range(2, int((N)**0.5)+1):
#  t=2
#  s=0
#  while s<=N:
#    s=i**t
#    if s==N:
#      r=max(r, t)
#      t=0
#      break
#    else:
#      t+=1
#print(r)