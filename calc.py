a=int(input(""));j=(input(" "));b=int(input(""))


l=ord(j)
def week(i):
    calc = {
        43: a+b,
        45: a-b,
        37: a%b,
        42: a*b,
        47: a/b,

    }
    return calc.get(i, "Invalid oprater")
print(week(l))
