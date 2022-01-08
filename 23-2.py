N = int(input())
arr = list(map(int, input().split()))
K = int(input())

count = 0
maxi = 0
for i in arr:
    if i < 0:
        count += 1
        if i < maxi:
            maxi = i

print(count)
if count > K:
    print(-maxi)