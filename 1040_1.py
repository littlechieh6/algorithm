def dfs(begin, end):
    # 如果在边界，即 begin = root 或 root = end。该情况为无子节点，所以返回为(1,0)。0代表无节点
    if end - begin < 0:
        return (1, 0)
    if (begin, end) in back_root:
        return back_root[(begin, end)]

    # begin和end相同，所以根必为begin。
    if begin == end:
        root = begin
        back_root[(begin, end)] = (num_list[begin], root)
        return (num_list[begin], begin)
    max_n, max_r = 0, 0
    # 遍历begin-end，找出值最大的根和分数
    for root in range(begin, end + 1):
        a = dfs(begin, root - 1)
        b = dfs(root + 1, end)
        temp = a[0] * b[0] + num_list[root]
        if temp > max_n:
            max_n = temp
            max_r = root
    # 保存节点的 root
    back_root[(begin, end)] = (max_n, max_r)
    return (max_n, max_r)


def print_root(begin, end):
    if end - begin < 0:
        return
    if end == begin:
        print(back_root[(begin, end)][1], end=" ")
        return

    root = back_root[(begin, end)][1]
    print(root, end=" ")
    print_root(begin, root - 1)
    print_root(root + 1, end)

if __name__ == '__main__':
    n = int(input())
    # 添加0，保证数字在序号1-n之间
    num_list = [0] + list(map(int, input().split()))
    back_root = {}
    res = dfs(1, n)
    print(res[0])
    print_root(1, n)
