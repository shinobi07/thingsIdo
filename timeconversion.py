def solve(a):
    b = ''
    if a[0] + a[1] == "12" and a[-2] + a[-1] == "AM":
        b += "00"
        for i in range(2, len(a) - 2):
            b += a[i]
    elif a[-2] + a[-1] == "AM":
        for i in range(len(a) - 2):
            b += a[i]
    elif a[0] + a[1] == "12" and a[-2] + a[-1] == "PM":
        for i in range(len(a) - 2):
            b += a[i]
    else:
        c = int(a[0] + a[1]) + 12
        b += str(c)
        for i in range(2, len(a) - 2):
            b += a[i]
    return b


while True:
    a = input()
    if a == "exit":
        break
    else:
        print(solve(a))