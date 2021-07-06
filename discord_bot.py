import discord
import os 
from datetime import datetime as dt

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
SEND_CH_ID = int(os.environ.get('SEND_CH_ID', 0))
VOICE_CH_ID = int(os.environ.get('VOICE_CH_ID', 0))


client = discord.Client()
member_time ={}

@client.event
async def on_ready():
    print('on_ready')

@client.event
async def on_voice_state_update(member, before, after):
    send_channel = client.get_channel(SEND_CH_ID)
    if after.channel != before.channel :
        if  after.channel is not None and after.channel.id== VOICE_CH_ID:
            member_time[member.id]=dt.now()
            msg = f'【{dt.now().strftime("%Y/%m/%d %H:%M:%S")}】 `{member.name}` が参加しました。'
            
            print(msg)
            await send_channel.send(msg)
        elif before.channel is not None and before.channel.id == VOICE_CH_ID:
            duration_time =  dt.now() - member_time[member.id]
            msg = f'【{dt.now().strftime("%Y/%m/%d %H:%M:%S")}】 `{member.name}` が退出しました。'
            msg += f'【通話時間 {duration_time.strftime("%H:%M:%S")}】'
            
            print(msg)
            await send_channel.send(msg)
    
client.run(TOKEN)
