b=input()
Lmin=Rmin=Lmax=Rmax=0
for i in range(3):
    if b[i]=='*':
        Lmin+=0
        Lmax+=9
    else:
        Lmin+=int(b[i])
        Lmax+=int(b[i])
    if b[i+3]=='*':
        Rmin+=0
        Rmax+=9
    else:
        Rmin+=int(b[i+3])
        Rmax+=int(b[i+3])
if Lmin<=Rmax and Lmax>=Rmin:
    print('Yes')
else:
    print('No')