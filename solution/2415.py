n_list = list(map(int, input().split()))
res = sum(list(map(lambda x: int(x) * pow(2, len(n_list) - 1), n_list)))
print(res)
