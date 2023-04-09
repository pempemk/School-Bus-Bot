import os
import discord
from discord.ext import commands
from discord.ui import Button, View
import time
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello! bot is ready")

@bot.command()
async def bus(ctx):
    button = Button(label='Join', style=discord.ButtonStyle.green, )
    button2 = Button(label='Lets Go', style=discord.ButtonStyle.red)
    list_name = []

    async def button_callback(interaction: discord.Interaction):
        await interaction.response.edit_message(content= f'Click the button to ride this bus!', view= view)
        member:discord.Member
        name = interaction.user
        list_name.append(name)
        for i in range(len(list_name)):
            member = list_name[i]
        await ctx.send(content= f'{member.display_name} Join this bus' )

    async def button_callback2(interaction: discord.Interaction):
        await interaction.response.edit_message(content= f'https://cdn.discordapp.com/attachments/1004335035048001556/1094358698178117773/-_Clipchamp_3.gif', view= None)
        member:discord.Member
        time.sleep(12)
        for i in range(len(list_name)):
            member = list_name[i]
            await member.move_to(None)
        await interaction.message.delete()

        
    button.callback = button_callback
    button2.callback = button_callback2
    
    view = View()
    view.add_item(button)
    view.add_item(button2)
    await ctx.send(content= 'Click the button to ride this bus!',view=view) 

Bot_token = os.getenv('BOT_TOKEN')
bot.run(Bot_token)