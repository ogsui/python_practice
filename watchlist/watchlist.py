try:
    with open("watchlist.txt", "r") as file:
        watchlist = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    watchlist = []


def menu():
    print("select an option\n")
    print("1) add to list\n")
    print("2) remove from list\n")
    print("3) view watchlist\n")
    print("4) exit")


while True:
    menu()
    choice = int(input("Enter your choice(1-4): "))

    if choice == 1:
        stock = input("enter stock: ").strip().upper()
        if stock not in watchlist:
            watchlist.append(stock)
            print(stock + " is added to watchlist")
        else:
            print(stock, "already in watchlist")

    elif choice == 2:
        stock = input("enter stock to remove: ").strip().upper()
        if stock in watchlist:
            watchlist.remove(stock)
            print(stock + " is removed from watchlist")
        else:
            print(stock, "is not in watchlist")

    elif choice == 3:
        if watchlist:
            print("watchlist")
            for i, stock in enumerate(watchlist, 1):
                print(f"{i} {stock}")
        else:
            print("watchlist is empty")

    elif choice == 4:
        with open("watchlist.txt", "w") as file:
            for stock in watchlist:
                file.write(stock + "\n")
            print("Watchlist saved to watchlist.txt. Goodbye!")
            break

    else:
        print("Invalid choice. Please enter 1–4.")