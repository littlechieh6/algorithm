GO = "GO"
STAY = "STAY"


def fun(string):
    n = 1
    for i in string:
        if i.isupper():
            num = ord(i) - 64
            n *= num
    return n


if __name__ == "__main__":
    ufo_name = input()
    team_name = input()
    ufo_num = fun(ufo_name)
    team_num = fun(team_name)
    if team_num % 47 == ufo_num % 47:
        print(GO)
    else:
        print(STAY)
