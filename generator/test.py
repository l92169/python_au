import sys
def calculate(first, second, oper):
    calc = {
        "+": first + second,
        "-": first - second,
        "*": first * second,
        "/": first / second,
    }
    return calc[oper]
'''def main(first, second, oper):
    if oper == "+":
        print(first, '+', second, '=', first + second)
    elif oper == "*":
        print(first, '*', second, '=', first * second)
    elif oper == "-":
        print(first, '-', second, '=', first - second)
    elif oper == "/":
        if second == 0:
            print("Error")
        else:
            print(first, '/', second, '=', first / second)'''


def main(first, second, oper):
    print(calculate(first, second, oper))


if __name__ == "__main__":
    params = sys.argv
    main(float(params[1]), float(params[2]), (params[3]))


