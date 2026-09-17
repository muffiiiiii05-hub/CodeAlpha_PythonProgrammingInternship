# Stock Portfolio Tracker

# Stock names and their prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 170,
    "MSFT": 400
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment = total_investment + investment

        print("Stock Price:", stock_prices[stock])
        print("Investment:", investment)

    else:
        print("Stock not available.")

print("\n------------------------------")
print("Total Investment Value:", total_investment)
print("------------------------------")
print("Thank you for using the program!")