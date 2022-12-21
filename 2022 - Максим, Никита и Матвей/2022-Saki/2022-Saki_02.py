str1=set(input())
str2=set(input())
s=''
for i in str1:
   if i in str2:
       s+=i
print(''.join(sorted(s))) if len(s) else print('epidemic')