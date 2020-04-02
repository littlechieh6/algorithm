n = int(input())
n_l = list(map(int, input().split()))
for i in range(n):
    s = 0
    for j in range(i):
        if n_l[j] < n_l[i]:
            s += 1
    print(s, end=" ")
