from itertools import combinations
n = int(input())
n_l = list(map(int, input().split()))
c_l = combinations(n_l, 2)
res = []
for l in c_l:
    s = sum(l)
    if s in n_l:
        res.append(s)
print(len(set(res)))
