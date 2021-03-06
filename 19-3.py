N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

start_counter = 0
max_counter = 1
last = 0

for i in range(N):
    if arr[i] > last:
        counter = 1
        last = arr[i]
        start_counter = i
    else:
        counter += 1
        if counter >= M:
            max_counter = M
            break
        if counter >= max_counter:
            if start_counter >= M - counter:
                max_counter = counter

print(M - max_counter)