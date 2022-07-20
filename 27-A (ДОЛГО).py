T = int(input())
for i in range(T):
  N = int(input())
  arr = []
  r = 11
  for j in range(N):
    s = input()
    if len(s) < r:
      r = len(s)
    for k in range(len(arr)):
      if s[:r] == arr[k][:r]:
        r = 'NO'
        break
    if r == 'NO':
      print('NO')
      break
    else:
      arr.append(s)
  if r != 'NO':
    print('YES')

# Не проходит по времени на 2 тесте
