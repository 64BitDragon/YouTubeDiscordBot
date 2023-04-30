import os

from find_video import find_video
#from keep_alive import keep_alive

import discord
from discord.ext import tasks

intents = discord.Intents.default()

url=[1,2,3,4,5]
previous_url = ['/watch?v=MJ23x2mhvl4', '/watch?v=zB-kK9popJQ', '/watch?v=dJV4M2QkTDs']

channel = "https://www.youtube.com/channel/UC14zSCww91iy_JMaM8aXImQ" #youtube game page
discord_channel = 1023243703189504124 #replace with ID of text channel you want to post to
discord_role = "<@&1030816878349791253>" #replace numbers with role ID

find_video(channel)
client = discord.Client(intents=intents)

my_secret = "" #your bot secret key

@client.event
async def on_ready():
  print(f"{client.user} logged in now!")
  loopie.start()
  
  
@client.event
async def on_message(message):#can be deleted
  
  if message.content.startswith("any videos?"):
    print("should work")
    #print(message.channel)
    
    await message.channel.send(f"Hello! How are you {message.author}")
      


@tasks.loop(hours=1)
async def loopie():
    print("work")
    url = find_video(channel)
    print(url)
    txtchannel =client.get_channel(discord_channel)
    message = discord_role + " "
    flag=0
    for i in range(len(url)):
        if url[i] in previous_url:
            print("No new video uploaded! (were already sent)")
        else:
            print("new video alert")
            message= message + "New video uploaded! Watch it here: https://www.youtube.com" + url[i] + " \n"
            if url!=[]:
                flag=1
                #await txtchannel.send(message)
            else:
                await txtchannel.send("No new video uploaded!")
            print(url[i])
            if len(previous_url) >=35:#remembers the last 35 videos.
                previous_url.pop(0)
            previous_url.append(url[i])
        print(previous_url)  
    if(flag==1):
        await txtchannel.send(message)
    
    print(url)
        #print("no new videos")
  


#print(client.get_channel(1023243703189504124))
#keep_alive()  
client.run(my_secret)
