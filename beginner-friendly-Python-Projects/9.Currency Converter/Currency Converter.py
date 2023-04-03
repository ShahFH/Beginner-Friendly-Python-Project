import requests

# replace YOUR_API_KEY with your actual API key
api_key = 'YOUR_API_KEY'

# enter the base currency code and the target currency code
base_currency = input('Enter the base currency: ')
target_currency = input('Enter the target currency: ')

# enter the amount to convert
amount = float(input('Enter the amount to convert: '))

# create the API request URL
url = f'https://api.exchangeratesapi.io/latest?base={base_currency}&symbols={target_currency}&access_key={api_key}'

# send the request and get the response
response = requests.get(url)

# get the conversion rate from the response
conversion_rate = response.json()['rates'][target_currency]

# calculate the converted amount
converted_amount = amount * conversion_rate

# print the result
print(f'{amount} {base_currency} is equal to {converted_amount} {target_currency}.')
