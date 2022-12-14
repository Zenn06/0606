# This example requires the 'message_content' intent.

import discord
import json
from fun_class import check__
class MyClient(discord.Client):
    global seesion,fun_c
    seesion = []
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global seesion
        print(f'Message from {message.author}: {message.content}')
        # if(mes)
        if(message.content == "//"):
           await message.channel.send("กรุณาพิมพ์จำนวนหินที่ต้องการ")
        #    seesion[message.author.name] = 1
           ob = {message.author.id:1}
           
        #    print(ob[message.author.id])
           seesion.append(ob)
           check__(seesion,message.author.id)
        #    print()
#8วย
        # print(message)
        #add commit push

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA1MDQwMjI5OTg3ODU5MjU2Mw.GdQL5t.zqbfrzLNuppArENvlUraXpBw0JLMniHkBlthiU')
