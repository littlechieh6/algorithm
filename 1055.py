s = input()
n = 1
r = 0
for i in [0,2,3,4,6,7,8,9,10]:
    r += int(s[i]) * n
    n += 1
r = r%11
if r == 10:
    r = "X"
if str(r) == s[12]:
    print("Right")
else:
    print(s[0:12] + str(r))
