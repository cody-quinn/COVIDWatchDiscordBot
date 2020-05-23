import discord, datetime
from bot.commands.command import Command


class SymptomsCMD(Command):
    async def run(self, message, raw_args):
        embed = discord.Embed(colour=discord.Colour(0x1d837e), timestamp=datetime.datetime.utcfromtimestamp(1589104767))

        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")
        embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                         icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

        embed.add_field(name="Information", value='''
                                COVID19 is a deadly virus that rapidly spreads and kills, here are the symptoms of the virus, if you experience one or many of these symptoms please get tested and seek medical advice. A very worrying part of COVID19 is that it takes up to 2 weeks before you have symptoms if you experience any at all
                            ''', inline=False)
        embed.add_field(name="Symptoms", value='''
                            **`1-`** A Cough\n**`2-`** Shortness in breath\n**`3-`** Fever\n**`4-`** Chills\n**`5-`** Repeated shaking with chills\n**`6-`** Muscle Pain\n**`7-`** Headache\n**`8-`** Sore throat\n**`9-`** Trouble breathing\n**`10-`** Persistent pain or pressure in the chest\n**`11-`** New confusion or inability to arouse\n**`12-`** Bluish lips or face
                            ''')

        await message.channel.send(content="‌‌ \n**`Coronavirus Symptoms`**\n*`Please stay safe`*", embed=embed)