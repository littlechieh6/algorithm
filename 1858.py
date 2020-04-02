n = 9
n_l = [2,2,4,6,2]
max_s = 0

def dp(k, s):
    global max_s
    if k == 5 or s==n:
        if s > max_s:
            max_s = s
        return
    print(k, s)
    dp(k+1, s)
    if s+n_l[k]<=n:
        dp(k+1, s+n_l[k])


dp(0, 0)
print(max_s)
