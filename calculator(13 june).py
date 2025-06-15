num1 = float(input("enter a number:"))
sign = str(input("enter a arithmetic operator(+.-.x./) "))
num2 = float(input("enter another number:"))

def calculator():
    if sign == "x":
        print(num1*num2)
    elif sign == "-":
        print(num1-num2)
    elif sign == "+":
        print(num1+num2)
    elif sign == "/":
        print(num1/num2)
    else:
        print("enter valid operator")

calculator()