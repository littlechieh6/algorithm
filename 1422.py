def fun(x):
    res = 0
    if x <= 150:
        res = x * 0.4463
    elif x > 150 and x <= 400:
        res = 150 * 0.4463 + (x-150) * 0.4663
    elif x > 400:
        res = 150 * 0.4463 + 250 * 0.4663 + (x-400) * 0.5663
    return res


x = int(input())
print("{:.1f}".format(fun(x)))
