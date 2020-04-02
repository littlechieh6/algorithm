n = int(input())
n_l = list(map(int, input().split()))
d = 0
d_max = 0
c = 0
for i in n_l:
    if i>=c:
        d += 1
        c = i
    else:
        if d_max<d:
            d_max = d
        d = 1
        c = i
print(d_max)
