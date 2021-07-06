# voice_channel_notification_for_discord

## これはなに?

特定のボイスチャンネルに誰かが参加、退出したら、テキストチャンネルに通知するdiscordbot

## 使用方法

### 環境変数の設定
以下の値を環境変数に設定してください

|key|value|
|:-|:-|
|DISCORD_BOT_TOKEN| discordのbotのtoken|
|SEND_CH_ID|通知するテキストチャンネルのid|
|VOICE_CH_ID|監視するボイスチャンエンルのid|


### pipenvを使う場合

```
$pipenv install
$pipenv run python discord_bot.py
```

### pipenvを使わない場合

```
$pip install -r requirements.txt
$python discord_bot.py
```

