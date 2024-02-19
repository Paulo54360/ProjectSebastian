import discord
import asyncio

class TrombiView(discord.ui.View):
    def __init__(self, message, bot):
        super().__init__()
        self.message = message
        self.filExplained = False
        self.messageAt = None
        self.bot = bot
        asyncio.create_task(self.delete_after_delay(delay=30))
    async def delete_after_delay(self, delay):
        await asyncio.sleep(delay)
        if self.filExplained == False:
            try:
                await self.messageAt.delete()
                await self.message.delete()
            except Exception:
                pass

    @discord.ui.button(label="J'ai compris",
                       style=discord.ButtonStyle.green)
    async def button_compris(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.name == self.message.author.name:
            try:
                await self.messageAt.delete()
                await self.message.delete()
            except Exception:
                pass
        else:
            embed = discord.Embed(title="Pas toi !",
                                  description=f"Tu n'est pas le criminel !",
                                  colour=0xFF6868)
            await interaction.response.send_message(embed=embed,ephemeral=True)

    @discord.ui.button(label="C'est quoi un fil ?",
                       style=discord.ButtonStyle.primary)
    async def button_fil(self, interaction: discord.Interaction, button: discord.ui.Button):

        if not self.filExplained and self.message.author == interaction.user:
            self.filExplained == True

        try:
            await self.message.channel.fetch_message(self.message.id)

            if self.message.flags.has_thread :
                my_thread = self.bot.get_channel(self.message.id)
                await my_thread.send(f"Je t'écris ce message dans un fil {interaction.user.mention}.\nUn fil sur Discord est une sous-discussion créée à partir d'un message dans un canal, permettant d'organiser des conversations spécifiques sans encombrer le canal principal.")
            else:
                my_thread = await self.message.create_thread(name="Ceci est un fil")

            await interaction.response.send_message(f"Va voir le fil : {my_thread.mention}", ephemeral=True)

        except discord.NotFound:

            await interaction.response.send_message(f":Un fil sur Discord est une sous-discussion", ephemeral=True)



class TrombiViewFormat(discord.ui.View):
    def __init__(self, message):
        super().__init__()
        self.message = message
        self.messageAt = None
        asyncio.create_task(self.delete_after_delay(delay=30))
    async def delete_after_delay(self, delay):
        await asyncio.sleep(delay)

    @discord.ui.button(label="J'ai compris",
                       style=discord.ButtonStyle.green)
    async def button_compris(self, interaction: discord.Interaction, button: discord.ui.Button):

        if interaction.user.name == self.message.author.name:
            try:
                await self.messageAt.delete()
                await self.message.delete()
            except Exception:
                pass
        else:
            embed = discord.Embed(title="Pas toi !",
                                  description=f"Tu n'est pas le criminel !",
                                  colour=0xFF6868)
            await interaction.response.send_message(embed=embed,ephemeral=True)






