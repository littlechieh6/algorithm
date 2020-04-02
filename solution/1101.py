n = int(input())
my = "yizhong"

s_l = ["-"*(n+2)]
stand = []
for i in range(n):
    s = input()
    if s == "\n":
        continue
    s_l.append("|"+s+"|")
    stand.append(s)
s_l.append("-"*(n+2))


res = [[False]*n for i in range(n)]

d_l = ((1, 0), (1, -1), (0, -1), (-1,-1), (-1, 0), (-1,1), (0, 1), (1, 1))


def dfs(x, y, k):
    s = ""
    for i in range(7):
        a = x+d_l[k][0]*i
        b = y+d_l[k][1]*i
        if a>=n+1 or b>=n+1 or a<=0 or a<=0:
            return
        s+=s_l[a][b]
    if s == my:
        for i in range(7):
            a = x+d_l[k][0]*i
            b = y+d_l[k][1]*i
            res[a-1][b-1] = True

    


for i in range(n+2):
    for j in range(n+2):
        if s_l[i][j] != "y":
            continue
        for k in range(8):
            x = i+d_l[k][0]
            y = j+d_l[k][1]
            if s_l[x][y] == "i":
                dfs(i, j, k)


for i in range(n):
    for j in range(n):
        if res[i][j]:
            print(stand[i][j], end="")
        else:
            print("*", end="")
    print()
