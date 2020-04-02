"""
关键词：动态规划、状态转移表
"""

n = int(input())
f = [[0] * (n + 1) for i in range(n + 1)]
root = [[0] * (n + 1) for i in range(n + 1)]
# 初始化区间最大值 和 该区域最大时根的号数。
s = list(map(int, input().split()))
for i in range(1, n + 1):
    f[i][i] = s[i - 1]
    f[i][i - 1] = 1
    root[i][i] = i

for l in range(1, n):
    for i in range(1, n - l + 1):
        j = i + l
        # 设置默认值
        f[i][j] = f[i + 1][j] + f[i][i]
        root[i][j] = i
        # 遍历该区间的所有值，找到最大值，以及最大点。
        for k in range(i + 1, j):
            if f[i][j] < f[i][k - 1] * f[k + 1][j] + f[k][k]:
                f[i][j] = f[i][k - 1] * f[k + 1][j] + f[k][k]
                # k 代表第几个节点（横坐标）
                root[i][j] = k


def print_f(b, e):
    if b > e:
        return
    # 递归输出（前序遍历）
    print(root[b][e], end=" ")
    print_f(b, root[b][e] - 1)
    print_f(root[b][e] + 1, e)


print(f[1][n])
print_f(1, n)

for p in range(0, n + 1):
    print(f[p])
print("-------------------")