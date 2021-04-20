from PIL import Image, ImageFont, ImageDraw
import requests

#currency_image = Image.open(urlopen('https://i.imgur.com/175owdY.png'))
# currency_image.show()

""" currency_image = Image.open("currency_bg.png")
font = ImageFont.truetype("RobotoMono-Medium.ttf", 36)

draw = ImageDraw.Draw(currency_image)
text = "testing stuff"

draw.text((160, 40), text, (0, 0, 0), font=font)
currency_image.save("converted.png")

currency_image.show() """


class CurrencyConverter():

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['conversion_rates']

    def convert(self, from_currency: str, to_currency: str, amount: float):
        initial_amount = amount
        # first convert it into USD if it is not in USD.
        # because our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # limiting the precision to 4 decimal places
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


url = 'https://v6.exchangerate-api.com/v6/44d79dac0171c98f3cdf7717/latest/USD'

converter = CurrencyConverter(url)

print(converter.convert('USD', 'EUR', 100))
