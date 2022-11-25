import discord
import discord.utils
from discord import app_commands
import json

TOKEN = json.load(open("config.json"))["TOKEN"]


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}")


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='hello')
async def self(interaction: discord.Interaction):

    # Send interaction
    await interaction.response.send_message(f"Hello {interaction.user.name}!")

# Run bot
client.run(TOKEN)
