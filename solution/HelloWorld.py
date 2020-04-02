def dfs(begin, end):
    # 如果在最边上（左或右）
    if begin > end:
        return (1, 0)
    if end < begin:
        return (1, n)
    if begin == end:
        return (s[begin], begin)
    if (begin, end) in back:
        return back[(begin, end)]
    max_n = 0
    max_r = -1
    # 使每个点作为根节点
    for root in range(begin, end + 1):
        a = dfs(begin, root - 1)
        b = dfs(root + 1, end)
        temp = a[0] * b[0] + s[root]
        print(root, a, b, temp)
        if max_n < temp:
            max_n = temp
            max_r = root
            # 保存其左右的根节点
            backup[root] = (a[1], b[1])
            back[(begin, end)] = (max_n, max_r)
    # 返回最大值，还有最大值对应的根
    return (max_n, max_r)


def print_root(root):
    l = backup[root][0]
    r = backup[root][1]
    if l is not 0:
        print_root(l)
    print(root)
    if r is not 0:
        print_root(r)


n = int(input())
back = {}
backup = {}
# 添加0，保证数字在序号1-n之间
s = [0] + list(map(int, input().split()))
res = dfs(1, n)
print(res[0])
print(backup)
# print_root(res[1])
