import discord
from discord import app_commands
from discord.ext import commands

import vars
from classes import *

#✅ ⬜ ❌ 👍 👋 👀 ⚠️ ❤️ 🔥 👉 👇 🎉 📢

bot = commands.Bot(command_prefix="$", intents = discord.Intents.all()
)

@bot.event
async def on_ready():
    print("Your bot has logged in !")
    await sync()

async def sync():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message):

    # Gestion des messages utilisateurs
    if not message.author.bot:

        # Gestion des messages envoyés dans le trombinoscope

        if message.channel.name == "📸・trombinoscope":

            if message.attachments :

                if all(attachment.filename.endswith(('.png', '.jpg', '.jpeg', '.mp4', '.mov')) for attachment in message.attachments):
                    await message.create_thread(name="💬 Espace commentaire de la publication")
                else:
                    embed = discord.Embed(title="Tu ne peux pas poster ça ici",
                                  description=f"{message.author.mention} Merci d'envoyer des fichiers uniquement sous ces formats :\n**.png\n.jpg\n.jpeg\n.mp4\n.mov**",
                                  colour=0xFF6868)

                    view = TrombiViewFormat(message=message)
                    s_message = await message.channel.send(embed=embed, view=view)
                    view.messageAt = s_message
            else:
                embed = discord.Embed(title="Ecris ton message dans le fil de la photo/vidéo !",
                                    description=f"Salut {message.author.mention}, la prochaine fois, pense à écrire ton message dans les fils de discussion que je crée sous les photos et les vidéos afin de garder ce salon plus facilement lisible et propre.",
                                    colour=0xFF6868)

                view = TrombiView(message=message, bot = bot)

                s_message = await message.channel.send(embed=embed,view=view)

                view.messageAt = s_message

    await bot.process_commands(message)


bot.run(vars.TOKEN)
