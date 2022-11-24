arr=[]
for y in range(3):
    for x in input().split():
        arr.append(int(x))
for i in range(9):
    for j in range(i+1, 9):
        arr[i], arr[j]=arr[j], arr[i]
        if sum(arr[0:3])==sum(arr[3:6])==sum(arr[6:9]) and sum(arr[0:7:3])==sum(arr[1:8:3])==sum(arr[2:9:3]):
            break
        else:
            arr[i], arr[j]=arr[j], arr[i]
for i in range(0, 9, 3):
    print(arr[i], arr[i+1], arr[i+2])