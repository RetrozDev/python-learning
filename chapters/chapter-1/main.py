# Simple Currency Converter

# Exchange rates (example: 1 USD to other currencies)
rates = {
    "EUR": 0.86,
    "GBP": 0.75,
    "JPY": 152.57
}

# User input
amount_usd = float(input("Enter amount in USD: "))
target_currency = input("Convert to (EUR/GBP/JPY): ").upper()

# Conversion
if target_currency in rates:
    converted_amount = amount_usd * rates[target_currency]
    print(f"{amount_usd} USD = {converted_amount:.2f} {target_currency}")
else:
    print("Currency not supported.")
