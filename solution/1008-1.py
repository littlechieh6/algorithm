for i in range(123, 333):
    n = i
    if "0" in list(str(n)+str(n*2)+str(n*3)):
        continue
    if len(set(list(str(n)+str(n*2)+str(n*3)))) == 9:
        print(n, n*2, n*3)
