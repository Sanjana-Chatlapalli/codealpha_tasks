stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 120
}

total = 0

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        value = stocks[name] * quantity
        total += value
    else:
        print("Stock not found")

print("Total Investment Value:", total)

file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total))
file.close()