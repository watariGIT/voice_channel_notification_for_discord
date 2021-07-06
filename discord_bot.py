import discord
import os 

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
SEND_CH_ID = int(os.environ.get('SEND_CH_ID', 0))
VOICE_CH_ID = int(os.environ.get('VOICE_CH_ID', 0))

# 接続に必要なオブジェクトを生成
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print('on_ready')

@client.event
async def on_voice_state_update(member, before, after):
    send_channel = client.get_channel(SEND_CH_ID)
    if  after.channel is not None and after.channel.id== VOICE_CH_ID:
        msg = f'{member.name} が参加しました。'
        await send_channel.send(msg)
    elif before.channel is not None and before.channel.id == VOICE_CH_ID:
        msg = f'{member.name} が退出しました。'
        await send_channel.send(msg)

client.run(TOKEN)
