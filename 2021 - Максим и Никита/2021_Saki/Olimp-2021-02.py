arr=[]
for y in range(3):
    for x in input().split():
        arr.append(int(x))
for i in range(9):
    for j in range(i+1, 9):
        arr[i], arr[j]=arr[j], arr[i]
        if sum(arr[0:3])==sum(arr[3:6])==sum(arr[6:9]) and arr[0]+arr[3]+arr[6]==arr[1]+arr[4]+arr[7]==arr[2]+arr[5]+arr[8]:
            break
        else:
            arr[i], arr[j]=arr[j], arr[i]
for i in range(0, 9, 3):
    print(str(arr[i])+' '+str(arr[i+1])+' '+str(arr[i+2]))