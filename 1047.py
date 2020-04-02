L, M= map(int, input().split())
tree = [True]*(L+1)
for i in range(M):
    a, b=map(int, input().split())
    for j in range(a, b+1):
        if tree[j]:
            tree[j] = False
print(tree.count(True))
