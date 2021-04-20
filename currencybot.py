import requests
import discord
from discord.ext import commands
import json
#import forex_python
#from forex_python.converter import CurrencyRates
#from forex_python.converter import CurrencyCodes
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

@client.command(brief="testing stuff...")
async def testing_convert(ctx, first_currency: str, second_currency: str, value: float):

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


@client.command(brief="WORKING ONE")
async def convert(ctx, first_currency: str, second_currency: str, value: float):

    first_currency = first_currency.upper()
    second_currency = second_currency.upper()

    print(f'{first_currency} + {second_currency}')

    currency_converted = converter.convert(
        first_currency, second_currency, value)

    print(f'{currency_converted}')

    first_symbol = symbol.get_symbol(first_currency)
    second_symbol = symbol.get_symbol(second_currency)

    await ctx.send(f"{value}{first_symbol} to {second_symbol} is equal to {currency_converted}{second_symbol}")

 # do the float thingy yaknow .2f and then add the image manipulator with pillow


# YOU GET ERRORS HERE
""" @client.command(brief='Convert a currency to another. Converting 5 euro to usd would look like this $eur usd 5', aliases=['c', 'conversion', 'conv', 'C', 'CONV', 'conv', 'CONVERSION', 'CONVERT'])
async def converter(ctx, first_currency: str, second_currency: str, value: float):

    # here you want to .upper them for it to be acceptable?
    first_currency.upper()
    second_currency.upper()

    # here you want to convert the input currencies and values.
    currency_conversion = converter.convert(
        first_currency, second_currency, value)
 """

# ICI CODE TOUT DE BASE


# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT
# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT
# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT
# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT
# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT
# EN BAS N'EST PAS IMPORTANT POUR L'INSTANT


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


""" @client.command(aliases=['c', 'conv', 'C', 'CONV', 'CON', 'con', 'conversion'], brief="A converter built with the python forex framework, meant for learning")
async def convert(ctx, currency_name: str, currency_value: float):

    #random_message_number = random.randint(0, len(random_message) - 1)
    currency_name.upper()

    currency_converted = converter.convert(
        currency_name, 'TRY', currency_value)

    currency_symbol = codes.get_symbol(currency_name)

    currency_image = Image.open("currency_bg.png")
    font = ImageFont.truetype("RobotoMono-Medium.ttf", 36)

    draw = ImageDraw.Draw(currency_image)

    text.upper()

    text = f"{currency_value}{currency_symbol} = {currency_converted:.2f}"

    draw.text((160, 40), text, (0, 0, 0), font=font)
    currency_image.save("image.png")

    currency_embed = discord.Embed(
        title="annen", color=0x4200BD)  # creates embed
    file = discord.File("image.png", filename="image.png")
    currency_embed.set_image(url="attachment://image.png")
    # await ctx.send(file=file, embed=embed)

    await ctx.send(embed=currency_embed) """


""" currency_converter_embed = discord.Embed(
        title=f"Converting: {currency_value}-{currency_symbol} is equal to {currency_converted:.2f}₺",
        #title=f"Converting: {currency_value} of {currency_symbol} ({currency_name}) is equal to {currency_converted:.2f}₺ (TRY)",
        #description=f"Converting {currency_value} of {currency_symbol} ({currency_name}) to ₺ (TRY), {random_message[random_message_number]}",
        color=0x4200BD
    ) """


""" @client.command(brief='Convert a currency to another. Converting 5 euro to usd would look like this $eur usd 5', aliases=['c', 'conversion', 'conv', 'C', 'CONV', 'conv', 'CONVERSION', 'CONVERT'])
async def convert(ctx, first_currency: str, second_currency: str, value: float):

    first_currency.upper()
    second_currency.upper()

    currency_converted = converter.convert()

    currency_image = Image.open("currency_bg.png")
    font = ImageFont.truetype("RobotoMono-Medium.ttf", 36)

    draw = ImageDraw.Draw(currency_image)

    draw.text((160, 40), text, (0, 0, 0), font=font)
    currency_image.save("image.png")

    text.upper()

    embed = discord.Embed(title="Title", description="Desc",
                          color=0x00ff00)  # creates embed
    file = discord.File("image.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed) """


client.run(TOKEN)
