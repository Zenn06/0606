# This example requires the 'message_content' intent.

import discord
from room import st
from fun_class import check__
from fun_class import token
from fun_class import rm_perm
class MyClient(discord.Client):
    global seesion,fun_c
    seesion = []
    async def embed(self,ctx,value):
      a = st(value)
      wen = a.wenn_commas()
      bp = a.blue_p_commas()

      embed=discord.Embed(
         title="Result", 
         # url="https://realdrewdata.medium.com/", 
         description='Wen = '+ str(wen) + " wen\nยาฟ้า = " + str(bp) + " ขวด", 
         color=0x4169E1)

      await ctx.send(embed=embed)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.bot:
         return

        global seesion
      #   print(f'Message from {message.author}: {message.content}')
        # if(mes)
      #   print()
        if check__(seesion,message.author.id).value:
         # print("111")
         # a = st(message.content)
         # await message.channel.send(a.wenn_commas())
         await self.embed(message.channel,message.content)
         seesion = rm_perm(seesion,message.author.id).args
         # print(a.wen_commas())
         # print(a.wenn_commas())

         #seesion = [zenzen01,zenzen02]
         #new_seesion = [zenzen02]
         #seesion = new_seesion
         

        else:
         # print("222")
         if(message.content == "//"):
           await message.channel.send("กรุณาพิมพ์จำนวนหินที่ต้องการ")
           ob = {message.author.id:1}
           seesion.append(ob)
         # return

        
           
        #    print()
#8วย
        # print(message)
        #add commit push

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token().token)
# print(token())
