t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    
    s = int((1 + n * m) * n * m / 2)
    ps = s / 2
    
    v = m // 2
    v2 = v + 1
    sLeftCol = int((1 + (n - 1) * m + 1) * n / 2)
    sRightCol = int((v + (n - 1) * m + v) * n / 2)
    sRightCol2 = int((v2 + (n - 1) * m + v2) * n / 2)
    sLeft = int((sLeftCol + sRightCol) * v / 2)
    sRight = int((sLeftCol + sRightCol2) * v2 / 2)
    rLeft = min(abs(ps - sLeft), abs(ps - (s-sLeft)))
    rRight = min(abs(ps - sRight), abs(ps - (s - sRight)))
    if rLeft <= rRight:
        minLR = rLeft
        minV = v
    else:
        minLR = rRight
        minV = v2
    
    h = n // 2 * 0 + int(n * 0.7066667) #####################
    h2 = h + 1
    sTop = int((1 + h * m) * h * m / 2)
    sBottom = int((1 + h2 * m) * h2 * m / 2)
    rTop = min(abs(ps - sTop), abs(ps - (s - sTop)))
    rBottom = min(abs(ps - sBottom), abs(ps - (s - sBottom)))
    if rTop <= rBottom:
        minTB = rTop
        minH = h
    else:
        minTB = rBottom
        minH = h2
    
    if minLR <= minTB:
        print('V', minV)
    else:
        print('H', minH)
