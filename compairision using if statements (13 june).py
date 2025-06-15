def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        print(f"{num1} is the greatest")
        return num1
    elif num2>=num3 and num2>=num1:
        print(f"{num2} is the greatest")
        return num2
    else:
        print(f"{num3} is the greatest")
        return num3

max_num(90,10,9)