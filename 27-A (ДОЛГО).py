T = int(input())
for i in range(T):
  N = int(input())
  arr = []
  r = 22222
  for j in range(N):
    s = input()
    if len(s) < r:
      r = len(s)
    for k in range(len(arr)):
      if s[:r] == arr[k][:r]:
        r = -1
        break
    if r == -1:
      print('NO')
      break
    else:
      arr.append(s[:r])
  if r > 0:
    print('YES')

# Не проходит по времени на 2 тесте
# ... нужно дерево
