s = input()
l = len(s)
if "." in s:
    a, b = s.split(".")
    r, k = 0,1
    for i in a:
        r += int(i) * k
        k*=10
    new = str(r) + "."
    r, k = 0, 1
    f = False
    for i in b:
        if i == "0" and f is False:
            continue
        if i!="0" and f is False:
            f = True
        r += int(i) * k
        k*=10
    new = new+str(r)
elif "/" in s:
    a, b = s.split("/")
    r, k = 0,1
    for i in a:
        r += int(i) * k
        k*=10
    new = str(r) + "/"
    r, k = 0, 1
    f = False
    for i in b:
        if i == "0" and f is False:
            continue
        if i!="0" and f is False:
            f = True
        r += int(i) * k
        k*=10
    new = new+str(r)
elif "%" in s:
    r, k = 0, 1
    for i in s[:-1]:
        r += int(i) * k
        k*=10
    new = str(r) + "%"
else:
    r, k = 0, 1
    for i in s:
        r += int(i) * k
        k*=10
    new = str(r)
print(new)
