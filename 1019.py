def time(h, s):
    c = 0
    p = 0
    for i in range(len(h)):
        a = i
        while s[p] == h[a]:
            p += 1
            a += 1
            if a>len(h) - 1:
                break
            if p == len(s) - 1:
                c+=1
                break
        p = 0
    return c
            



def check(h, s):
    t = False
    f = 0
    if h not in s and s not in h or time(h, s) < 2:
        for i in range(min(len(s), len(h)) - 1):
            if h[len(h) - 1 - i:] == s[:i+1]:
                f = i+1
                break
    return f

def fun(h):
    global m
    for s in ls:
        f = check(h, s)
        if f==0:
            continue
        else:
            fun(h+s[f:])
    l = len(h)
    if l>m:
        m = l
    return

n = int(input())
ls = []
for i in range(n):
    s = input()
    if s == "\n":
        continue
    ls.append(s)
h = input()
for s in ls:
    if h == s[0]:
        h = s
m = 0
fun(h)
print(m)
