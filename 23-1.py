S, A, B = map(int, input().split())
if S % A < S % B:
    print(1)
elif S % B < S % A:
    print(2)
else:
    print(0)