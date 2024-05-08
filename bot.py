import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@client.command(pass_context=True)
async def play(ctx, url):
    author = ctx.message.author
    voice_channel = author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            URL = info['formats'][0]['url']

        vc.play(FFmpegPCMAudio(URL))
    else:
        await ctx.send('Вы должны быть в голосовом канале, чтобы использовать эту команду.')


client.run('token')