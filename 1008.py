from itertools import permutations
import time
start = time.perf_counter()
p_l = permutations(range(1, 10), 3)
all_p = []
for i in p_l:
    all_p.append(i[0]*100+i[1]*10+i[2])
for i in all_p:
    if i>=333:
        break
    if i*2 in all_p and i*3 in all_p and len(set(list(str(i)+str(i*2)+str(i*3)))) == 9:
        print(i, i*2, i*3)
print(f"{time.perf_counter() - start}")
