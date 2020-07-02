"""
This module creates a discord bot, that can perform mathematical operations

Activate the bot by simply running this file

Commands for the bot:

!documentation ---- displays documentation of this file
!how_are_you ---- the bot says how he is
!who_is_my_lord ---- the bot says who its lord is
!I_love_you ---- says that he likes the user back
!calculator_add ---- accepts 2 integers as parameters and then adds them
!calculator_substract ---- accepts 2 integers as parameters and then subtracts them
!calculator_multiply ---- accepts 2 integers as parameters and then multiplies them
!calculator_divide ---- accepts 2 integers as parameters and then divides them them
!calculator_factorial ---- accepts 1 integer as parameter and finds factorial of this number
!calculator_square_root ---- accepts 1 integers as parameter and finds its square root


"""

import os
import random, math
from dotenv import load_dotenv
from discord.ext import commands

# Authentication
TOKEN = ""  #Enter your Discord Bot Token in here

# creating bot object
bot = commands.Bot(command_prefix='!')

@bot.command(name='documentation')
async def How_are_you(ctx):
    response = """
    !documentation ---- displays documentation of this file
    !how_are_you ---- the bot says how he is
    !who_is_my_lord ---- the bot says who its lord is
    !I_love_you ---- says that he likes the user back
    !calculator_add ---- accepts 2 integers as parameters and then adds them
    !calculator_substract ---- accepts 2 integers as parameters and then subtracts them
    !calculator_multiply ---- accepts 2 integers as parameters and then multiplies them
    !calculator_divide ---- accepts 2 integers as parameters and then divides them them
    !calculator_factorial ---- accepts 1 integer as parameter and finds factorial of this number
    !calculator_square_root ---- accepts 1 integers as parameter and finds its square root
"""
    await ctx.send(response)

@bot.command(name='how_are_you')
async def How_are_you(ctx):
    response = "I am doing great. What about you?"
    await ctx.send(response)

@bot.command(name='who_is_my_lord')
async def How_are_you(ctx):
    response = "My lords are Azim Ibragimov and Mr. Putin"
    await ctx.send(response)

@bot.command(name='I_love_you')
async def How_are_you(ctx):
    response = "Aww.... I love you too"
    await ctx.send(response)

@bot.command(name='calculator_add')
async def roll(ctx, number1: int, number2: int):
    response = number1+number2
    await ctx.send("The answer is " + str(response))

@bot.command(name='calculator_substract')
async def roll(ctx, number1: int, number2: int):
    response = number1-number2
    await ctx.send("The answer is " + str(response))

@bot.command(name='calculator_multiply')
async def roll(ctx, number1: int, number2: int):
    response = number1*number2
    await ctx.send("The answer is " + str(response))

@bot.command(name='calculator_divide')
async def roll(ctx, number1: int, number2: int):
    if number2 == 2:
        response == "You cannot divide by 0"
    response = number1/number2
    await ctx.send("The answer is " + str(response))

@bot.command(name='calculator_factorial')
async def roll(ctx, number1: int):
    response = math.factorial(number1)
    await ctx.send("The answer is " + str(response))

@bot.command(name='calculator_square_root')
async def roll(ctx, number1: int):
    response = math.sqrt(number1)
    await ctx.send("The answer is " + str(response))



bot.run(TOKEN)
