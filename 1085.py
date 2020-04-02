def fun(n_l):
    a_max = 0
    a_day = 0
    for i in range(7):
        if n_l[i] - 8 > a_max:
            a_max = n_l[i-1]
            a_day = i + 1
    return a_day

n_l = []
for i in range(7):
    n_l.append(sum(map(int, input().split())))
print(fun(n_l))
