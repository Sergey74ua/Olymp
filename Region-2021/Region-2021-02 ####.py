t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    
    k = n * m    ;print('всего клеток -', k) ########
    s = int((1 + k) * k / 2)    ;print('сумма всех клеток -', s) ########
    ps = s / 2    ;print('половина всей суммы -', ps) ########
    
    sLeftCol = int((1 + (n - 1) * m + 1) * n / 2)    ;print('сумма левой колонки -', sLeftCol) ########
    v = m // 2    ;print('номер правой колонки -', v) ########
    sRightCol = int((v + (n - 1) * m + v) * n / 2)    ;print('сумма правой колонки -', sRightCol) ########
    sLeft = int((sLeftCol + sRightCol) * n / 2)     ;print('сумма слева -', sLeft) ########
    sRighr = s - sLeft    ;print('сумма справа -', sRighr) ########
    
    sTop = 0    ;print('сумма сверху -', sTop) ########
    sBottom = s - sTop    ;print('сумма снизу -', sBottom) ########