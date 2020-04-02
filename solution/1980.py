import time
n,x = input().split()
start = time.perf_counter()
s = 0
for i in range(1, int(n)+1):
    s += list(str(i)).count(x)
print(s)
