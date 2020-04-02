from copy import deepcopy
n, m, t = list(map(int, input().split()))
sx, sy, fx, fy = map(int, input().split())
d_l = ((1,0), (0, -1), (-1,0), (0,1))
res = 0
 
p_l = [[False]*(n+2)]
for i in range(n):
    p_l.append([False] + [True]*n + [False])
p_l.append([False]*(n+2))

for i in range(t):
    x, y = map(int, input().split())
    p_l[x][y] = False


def dfs(sx, sy, p_l):
    global res
    if sx==fx and sy == fy:
        res += 1
        return
    for i in range(4):
        px, py = sx+d_l[i][0], sy+d_l[i][1]
        if p_l[px][py]:
            p_l[sx][sy] = False
            dfs(px, py, deepcopy(p_l))
            

dfs(sx, sy, deepcopy(p_l))
print(res)
