# Stock Portfolio Tracker

# Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 2800, # Google
    "AMZN": 3300,  # Amazon
    "MSFT": 310    # Microsoft
}

def stock_tracker():
    total_investment = 0
    portfolio = {}

    print("📈 Welcome to Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()

        if stock == "DONE":
            break
        elif stock not in stock_prices:
            print("❌ Stock not available. Try again.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        # Calculate investment for this stock
        investment = stock_prices[stock] * quantity
        total_investment += investment

        # Save to portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity

        print(f"✅ Added {quantity} shares of {stock} worth ${investment}.")

    print("\n📊 Final Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares worth ${qty * stock_prices[stock]}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Optional: Save to file
    save = input("Do you want to save results to file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-----------------------\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares worth ${qty * stock_prices[stock]}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}\n")
        print("📂 Results saved to portfolio.txt")

# Run the tracker
stock_tracker()
