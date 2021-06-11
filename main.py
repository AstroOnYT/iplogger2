import discord
import random
import json
import colorama
import os
import requests
from discord.ext import commands
from colorama import Fore

os.system('cls')
colorama.init()

with open('config.json', 'r') as f:
	data = json.load(f)

token = data['token']
prefix = data['prefix']
f.close()

def verify_token():
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    r = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
    if r.status_code != 200:
    	print(f'{Fore.RED}Improper token has been passed!\n\nAdd a real human discord account!{Fore.RESET}')
    	input()

    else:
    	pass

verify_token()

bot = commands.Bot(prefix, self_bot=True)

@bot.event
async def on_ready():
	print(f'{Fore.YELLOW}Ready to log people! {Fore.RESET}|{Fore.RED} User: {bot.user}{Fore.RESET}')

@bot.command()
async def log(ctx):
    await ctx.message.delete()
    f = open('data/links.txt', 'r+')
    data1 = f.readlines()
    data1 = data1[0]
    data1 = data1.split('|')
    link1 = data1[0]
    code1 = data1[1]
    f.close()
    f = open('data/links.txt', 'r+')
    data2 = f.readlines()
    data2 = data2[1]
    data2 = data2.split('|')
    link2 = data2[0]
    code2 = data2[1]
    f.close()
    f = open('data/links.txt', 'r+')
    data3 = f.readlines()
    data3 = data3[2]
    data3 = data3.split('|')
    link3 = data3[0]
    code3 = data3[1]
    f.close()

    ch1 = [link1 + '|' + code1]
    ch2 = [link2 + '|' + code2]
    ch3 = [link3 + '|' + code3]

    lkch = random.choice([link1, link2, link3])
    cdch = random.choice([code1, code2, code3])

    final = [ch1, ch2, ch3]
    final = random.choice(final)
    final = str(final)[1:-1]
    em = discord.Embed(description = f'Send this link to your target: {lkch} | Tracking code: {cdch}', color = (0x16cc4b))
    await ctx.send(embed=em, delete_after=20)

bot.run(token, bot=False)