from discord import app_commands
from discord.ext import commands
import discord
import numpy as np
import logging

_log = logging.getLogger(__name__)


class Senders(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    # @help_command()
    async def dm_number(self, interaction: discord.Interaction,
                        start: int = 1,
                        end: int = 100,
                        alphabet: bool = False,
                        help: bool = False):
        """Send random number as DM.

        Parameters
        ----------
        interaction : discord.Interaction
            _description_
        start : int, optional
            Number to start, by default 1
        end : int, optional
            Number to end, by default 100
        alphabet: bool, optional
            Send alphabet instead of number
        help : bool, optional
            _description_, by default False
        """
        vocie = interaction.user.voice.channel
        await interaction.response.defer()
        if vocie:
            pop = np.arange(start, end + 1)
            members = [v for v in vocie.members if not v.bot]
            if len(pop) < len(members):
                await interaction.followup.send(
                    "Number of member is too large.")
            else:
                numbers = np.random.choice(pop,
                                           size=len(members),
                                           replace=False)
                m: discord.Member
                for m, n in zip(members, numbers):
                    _log.debug(f"Send {n} to {m.mention} as DM.")
                    try:
                        if alphabet:
                            await m.send(f"{interaction.user.mention} send you {chr(64+n)}.")
                        else:
                            await m.send(f"{interaction.user.mention} send you {n}.")
                    except discord.errors.Forbidden:
                        await interaction.followup.send(
                            f"Fail to send to {m.mention}.")
                await interaction.followup.send("Send numbers to User.")

        else:
            await interaction.followup.send("You don't join vocie channel.")


async def setup(bot):
    await bot.add_cog(Senders(bot))
