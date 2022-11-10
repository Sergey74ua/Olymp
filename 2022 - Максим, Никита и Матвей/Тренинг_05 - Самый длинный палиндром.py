arr='-'+'-'.join(input())+'-'
d=len(arr)
pal=[0]*d
c=r=m=0
for i in range(d):
    j=0 if i>c+r else min(pal[c-(i-c)], c+r-i)
    while i-j>0 and i+j<d-1 and arr[i-j-1]==arr[i+j+1]:
        j+=1
    if i+j>c+r:
        c,r=i,j
    pal[i]=j
    m=max(m, j)
print(m)

# arr='-'+'-'.join(input())+'-'
# d=len(arr)
# pal=[0]*d
# c=r=m=0
# for i in range(d):
    # j=0 if i>c+r else min(pal[c-(i-c)], c+r-i)
    # while i-j>0 and i+j<d-1 and arr[i-j-1]==arr[i+j+1]:
        # j+=1
    # if i+j>c+r:
        # c, r=i, j
    # pal[i]=j
    # m=max(m, j)
# print(m)

# Неполное решение - 19  Превышено максимальное время работы >3.000
# (просой перебор вариантов)
#N = input()
#maxi = 1
#for i in range(len(N)):
#    for j in range(i, len(N)):
#        test = N[i:j+1]
#        if len(test) > 1 and test == test[::-1]:
#            maxi = max(maxi, len(test))
#print(maxi)

# Неполное решение - 26 Превышено максимальное время работы >3.000
# (вариант с центром + радиусом и двумя циклами проверки для чет и нечет)
#N=input()
#s=0
#for i in range(len(N)):
#    t=-1
#    for j in range(min(i, len(N)-i-1)+1):
#        if N[i-j]==N[i+j]:
#            t+=2
#            s=max(s, t)
#            print('нечетное -', t, N[i-j:i+j+1]) # тест
#        else:
#            break
#    p=0
#    for j in range(min(i, len(N)-i)):
#        if N[i-j-1]==N[i+j]:
#            p+=2
#            s=max(s, p)
#            print('четное -', p, N[i-j-1:i+j+1]) # тест
#        else:
#            break
#    if s==len(N): # не помогло
#        break
#print(s)

# Неполное решение - 25 Превышено максимальное время работы >3.000
# (замена цикла четных вариантов на всегда нечетную строку)
#N=input()
#n='|'+'|'.join(N)+'|'
#d=len(n)
#s=0
#for i in range(d):
#    t=-1
#    for j in range(min(i, d-i-1)+1):
#        if n[i-j]==n[i+j]:
#            t+=1
#            s=max(s, t)
#        else:
#            break
#    if s==d: # не помогло
#        break
#print(s)

# Неполное решение - 26 Превышено максимальное время работы >3.000
# (мой вариант по YouTube/LeetCode)
#N=input()
#s=0
#for i in range(len(N)):
#    l, r=i, i
#    while l>=0 and r<len(N) and N[l]==N[r]:
#        l-=1
#        r+=1
#    p=len(N[l+1:r])
#    l, r=i, i+1
#    while l>=0 and r<len(N) and N[l]==N[r]:
#        l-=1
#        r+=1
#    t=len(N[l+1:r])
#    s=max(s, p, t)
#print(s)