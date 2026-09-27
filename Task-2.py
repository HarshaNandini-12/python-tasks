prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 400
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in prices:
        value = prices[name] * quantity
        total += value
        print(name, "value:", value)
    else:
        print("Stock not found")

print("Total Investment:", total)

file = open("portfolio.txt", "w")
file.write("Total Investment: " + str(total))
file.close()

print("Saved to portfolio.txt")