name = input("stock name: ")
def getreturn():
    day1 = float(input("your purchase price "))
    day2 = float(input("your selling/current price"))
    return ((day2-day1)/day1)*100

pnl = getreturn()
print(f"{name} has given you {pnl:.2f}% in return" )