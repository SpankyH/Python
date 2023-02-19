#ДОП. Вывести STALKER как S.T.A.LK.ER

a = "STALKER"
for i in a:
    if i == "S" or i == "T" or i == "A" or i == "K" or i == "R":
        print(i, end=".")
    else:
        print(i, end="")

print("")

print(a[0], end=".")
print(a[1], end=".")
print(a[2], end=".")
print(a[3:5], end=".")
print(a[5:7], end=".")