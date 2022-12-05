N, K = map(int, input().split())
s = str(1/N)
s=s[2:]
s=int(s)
s=bin(s)
s = str(s)
print(s)
s=s[2:]
print(s)
print(s[K:K+1])


#N, K = map(int, input().split())
#s = str(1/N)
#s = str(bin(int(s[2:])))
#print(s[K:K+1])