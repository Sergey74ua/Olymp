N = input()
maxi = 1
for i in range(len(N)):
    for j in range(i, len(N)):
        test = N[i:j+1]
        if len(test) > 1 and test == test[::-1]:
            if len(test) > maxi:
                maxi = len(test)
print(maxi)