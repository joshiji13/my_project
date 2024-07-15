import requests

api_key = "998861d13c2d44ceb37998ac8f558491"

url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

response = requests.get(url)

data = response.json()

exchange_rates = data["rates"]

available_currencies = ""

for currency in exchange_rates.keys():
    available_currencies += currency + ", "

available_currencies = available_currencies[:-2]  

print("Available currencies: " + available_currencies)
    
from_currency = input("Enter the base currency: ").upper()
to_currency = input("Enter the target currency: ").upper()
amount = float(input("Enter the amount to convert: "))

original_amount = amount / exchange_rates[from_currency]
converted_amount = original_amount * exchange_rates[to_currency]

print(f"{amount} {from_currency} = {converted_amount} {to_currency}")