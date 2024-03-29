import discord
import os 
from datetime import datetime as dt
import pytz

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
SEND_CH_ID = int(os.environ.get('SEND_CH_ID', 0))
VOICE_CH_ID = int(os.environ.get('VOICE_CH_ID', 0))

EMOJI_NYUUSITU = os.environ.get('EMOJI_NYUUSITU', '入室')
EMOJI_TAISITU = os.environ.get('EMOJI_TAISITU', '退室')
def get_h_m_s(td):
    m, s = divmod(td.seconds, 60)
    h, m = divmod(m, 60)
    return h, m, s

client = discord.Client()
member_time ={}

@client.event
async def on_ready():
    print('on_ready')

@client.event
async def on_voice_state_update(member, before, after):
    send_channel = client.get_channel(SEND_CH_ID)
    if after.channel != before.channel :
        now = dt.now(pytz.timezone('Asia/Tokyo'))
        
        if  after.channel is not None and after.channel.id== VOICE_CH_ID:
            member_time[member.id]= now
            msg = f'{EMOJI_NYUUSITU } `{member.name}`'
            print(msg)
            await send_channel.send(msg)
            
        elif before.channel is not None and before.channel.id == VOICE_CH_ID:
            dh, dm, ds =  get_h_m_s(now - member_time[member.id])
            msg = f'{EMOJI_TAISITU} `{member.name}`'
            msg = msg + f'【通話時間 {dh:02}:{dm:02}:{ds:02}】'
            print(msg)
            await send_channel.send(msg)
    
client.run(TOKEN)
