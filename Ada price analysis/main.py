import requests
from datetime import datetime
from twilio.rest import Client

account_sid = "AC5b1b978b0486c34cee2843eca5d5bab3"
auth_token = "a90135de2d6352670c407e5e0574535e"

client = Client(account_sid, auth_token)


STOCK_NAME = "ADA"
CURRENCY = "USD"
my_email = "13116.uzairhussainsiddiqui@gmail.com"
password = "Uzair13116"


z = datetime.now()
hour = z.strftime("%I")
pm = z.strftime("%p")


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = "LNU61O9DHQTAXUCC"

day = datetime.today().strftime("%d")
month = datetime.today().strftime("%m")
year = datetime.today().strftime("%Y")
x = f"{year}-{month}-{day}"
stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": STOCK_NAME,
    "market": CURRENCY,
    "apikey": STOCK_APIKEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)

try:
    ada = response.json()['Time Series (Digital Currency Daily)'][x]

    open_price = ada['1a. open (USD)'][:4]
    close_price = ada['4a. close (USD)'][:4]
    highest_price = ada['2a. high (USD)'][:4]
    lowest_price = ada['3a. low (USD)'][:4]

    LIST = f"\n1 ADA=\nOpening price:  {open_price}\nClosing price: {close_price}\nHighest price: {highest_price}\nLowest price: {lowest_price}"

    if open_price and close_price and highest_price and lowest_price < 1.60:
        message = client.messages \
            .create(
            body=f"Ada is now {LIST}",
            from_="+14156492104",
            to="+923403553839"
        )

except:
    pass








