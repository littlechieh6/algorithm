a, b, c, d = map(int, input().split())
all_b = a*60 + b
all_e = c*60 + d
t = all_e - all_b
print(t//60, t%60)
