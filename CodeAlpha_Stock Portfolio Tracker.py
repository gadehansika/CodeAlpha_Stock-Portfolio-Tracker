
# stock_tracker.py

# 1. Hardcoded stock prices
stock_prices = stock_prices = {
    "AAPL": 190,      # Apple
    "GOOGL": 175,     # Google
    "MSFT": 450,      # Microsoft
    "AMZN": 185,      # Amazon
    "TSLA": 220,      # Tesla
    "META": 500,      # Meta
    "NFLX": 650,      # Netflix
    "NVDA": 1200,     # NVIDIA
    "TCS": 4200,      # Tata Consultancy Services
    "INFY": 1650,     # Infosys
    "RELIANCE": 3100, # Reliance Industries
    "HDFCBANK": 1750, # HDFC Bank
    "ICICIBANK": 1250,# ICICI Bank
    "WIPRO": 550,     # Wipro
    "SBIN": 900       # State Bank of India
}    

print("=== My Stock Investment Tracker ===")
print("Available stocks:", list(stock_prices.keys()))

# 2. Get user input
stock_name = input("Enter stock symbol: ").upper() #we get the inputs from the users 
quantity = int(input("Enter quantity: "))

# 3. Calculate total
total_investment = 0
if quantity <=0:
    print("Error: Quantity must be greater than 0.")
if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity
    
    # 4. Display result
    print(f"---Calculation---\n")
    print(f"Stock: {stock_name}\n")
    print(f"Price per share: ${price}\n")
    print(f"Quantity: {quantity}\n")
    print(f"Total Investment: ${total_investment}\n")
else:
    print(f"Error: {stock_name} not found in price list.")

# 5. Optional file save
if total_investment > 0: # only save if valid stock
    
    save = input("Do you want to save? (yes/no): ").strip().lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Value: {total_investment}")
    print("Result saved to portfolio.txt")
else:
    print("Result not saved")
    with open("portfolio.txt", "r") as file:
        print(file.read())
    