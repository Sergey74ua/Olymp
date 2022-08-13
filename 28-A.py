A, B = map(int, input().split())
s = min(A%B, B-A%B)
mini = s
for i in range(-s, s):
    for j in range(-s, s):
        if (A+i)%(B+j) == 0:
            temp = abs(i)+abs(j)
            if temp < mini:
                mini = temp
print(mini)