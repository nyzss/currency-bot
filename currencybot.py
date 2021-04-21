import requests
import discord
from discord.ext import commands
import json
from PIL import Image, ImageFont, ImageDraw
import PIL
from urllib.request import urlopen
import os
from symbol import CurrencyCodes

with open('token.json', 'r') as token_file:
    token = json.load(token_file)

TOKEN = token['token']

client = discord.Client()
client = commands.Bot(command_prefix='$')

symbol = CurrencyCodes()


@client.event
async def on_ready():
    print('Currency Bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Currency Converting'))


# make a currency list here

""" currency_image = Image.open("currency_bg.png")
font = ImageFont.truetype("RobotoMono-Medium.ttf", 36)

draw = ImageDraw.Draw(currency_image)
text = "testing stuff"

draw.text((160, 40), text, (0, 0, 0), font=font)
currency_image.save("converted.png") """

# direkt link: https://i.imgur.com/175owdY.png


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
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


url = 'https://v6.exchangerate-api.com/v6/44d79dac0171c98f3cdf7717/latest/USD'

converter = CurrencyConverter(url)

print(f"{converter.convert('USD', 'EUR', 100)} + {symbol.get_symbol('USD')}")


# WE'RE GONNA EDIT THIS ONE, THEN PUSH IT TO THE OTHER

@client.command(brief="testing stuff...", aliases=['c', 'C', 'conv', 'CONV', 'CONVERT', 'conversion', 'CONVERSION'])
async def convert(ctx, first_currency: str, second_currency: str, value: float):

    first_currency = first_currency.upper()
    second_currency = second_currency.upper()

    print(f'{first_currency} + {second_currency}')

    currency_converted = float(converter.convert(
        first_currency, second_currency, value))

    print(f'{currency_converted}')

    first_symbol = symbol.get_symbol(first_currency)
    second_symbol = symbol.get_symbol(second_currency)

    # ^^^^^^^^ the whole currency converting is up here ^^^^^^^^

    currency_image = Image.open("currency_test.png")

    font = ImageFont.truetype("RobotoMono-Medium.ttf", 26)

    draw = ImageDraw.Draw(currency_image)

    """ currency_limited = round(currency_converted, 2)
    value_limited = round(value, 0) """

    text = f"{value}{first_symbol} to {second_symbol} : {currency_converted}{second_symbol}"

    draw.text((140, 40), text, (0, 0, 0), font=font)

    currency_image.save("image.png")

    # under this is just going to send images: |||

    image_embed = discord.Embed(color=0x939393)  # creates embed

    file = discord.File("image.png", filename="image.png")

    image_embed.set_image(url="attachment://image.png")

    # up here ^^ is going to send images

    await ctx.send(file=file, embed=image_embed)

    # the send is going to be under this comment

    # await ctx.send(f"{value}{first_symbol} to {second_symbol} : {currency_converted}{second_symbol}")


# ICI CODE TOUT DE BASE

# color = 0xE0E0E0 or #E0E0E0

@client.command(brief="Shows you a table of the currencies you can use.", aliases=['currencies', 'table'])
async def list(ctx):
    list_embed = discord.Embed(
        title=f"Currency Table",
        # description=f"",
        color=0xE0E0E0
    )
    list_embed.set_image(
        url="https://i.imgur.com/QDCPQfT.png")
    await ctx.send(embed=list_embed)


@client.event
@client.command(brief="WORKING ONE")
async def testing_convert(ctx, first_currency: str, second_currency: str, value: float):

    first_currency = first_currency.upper()
    second_currency = second_currency.upper()

    print(f'{first_currency} + {second_currency}')

    currency_converted = converter.convert(
        first_currency, second_currency, value)

    print(f'{currency_converted}')

    first_symbol = symbol.get_symbol(first_currency)
    second_symbol = symbol.get_symbol(second_currency)

    await ctx.send(f"{value}{first_symbol} to {second_symbol} is equal to {currency_converted}{second_symbol}")


@client.command()
async def test(ctx, *, text):

    currency_image = Image.open("currency_bg.png")
    font = ImageFont.truetype("RobotoMono-Medium.ttf", 32)

    draw = ImageDraw.Draw(currency_image)

    draw.text((160, 37), text, (0, 0, 0), font=font)
    currency_image.save("image.png")

    text.upper()

    embed = discord.Embed(color=0x939393)  # creates embed
    file = discord.File("image.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)


client.run(TOKEN)
