arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

A = 0
B = 0
for i in range(3):
    if arr1[i] > arr2[i]:
        A += 1
    elif arr2[i] > arr1[i]:
        B += 1

if A >= 2:
    print(1)
elif B >= 2:
    print(2)
else:
    print(0)