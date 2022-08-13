T = int(input())
for i in range(T):
    n, A = map(int, input().split())
    R = 0

    TEST = 0
    for j in str(int(''.join(['1']*n))*A):
        TEST += int(j)
    #print('ТУПАЯ ПРОВЕРКА - ', TEST)

    if len(str(A)) >= n:
        for j in str(int(''.join(['1']*n))*A):
            R += int(j)
        #print('простое умножение - ', int(''.join(['1']*n))*A)
    else:
        for j in str(int(''.join(['1']*len(str(A))))*A):
            R += int(j)
        #print('урезанное умножение - ', int(''.join(['1']*len(str(A))))*A)
        #print('сумма крайних - ', R)
        s = int(''.join(['1']*(len(str(A))+1)))*A
        #print('избыточное умножение с центральной(повторяющейся) цифрой - ', s)

        pos = len(str(s))//2
        #print('позиция повторяшки - ', pos)

        num = int(str(s)[pos])
        #print('цифра - повторяшка - ', num)

        count = int(n) - len(str(A))
        #print('число повторяшек - ', count)

        summ = count * num
        #print('сумма повторяшек - ', summ)

        R += summ
    print(R)