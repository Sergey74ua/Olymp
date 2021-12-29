k = int(input())
a, x = map(int, input().split())
b, y = map(int, input().split())

ab = max(k - a, 0) * x + max(k - b - a, 0) * y
ba = max(k - a - b, 0) * x + max(k - b, 0) * y

print(max(ab, ba))