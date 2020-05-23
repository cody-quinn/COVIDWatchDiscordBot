import discord, datetime
from bot.commands.command import Command


class HelpCMD(Command):
    async def run(self, message, raw_args):
        embed = discord.Embed(colour=discord.Colour(0x9c0519), timestamp=datetime.datetime.utcfromtimestamp(1589100774))
        embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_(black).svg/1200px-Question_mark_(black).svg.png")
        embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                         icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

        embed.add_field(name="> c;cases",
                        value="The 'cases' command will display a embed containing updated information about all the cases worldwide or in a selected region \n\n __**Modifiers**__\n     ***__`-country <target>`__***  -  Targets a specific country  (*Aliases:* **`-c`**)\n     ***__`-all`__***  -  Displays extra data, such as 'new' cases & 'new' deaths  (*Aliases:* **`-a`**)\n\n__**Example**__\n     **`c;cases -country US -all`**  -  Will target the USA and display all information including New Cases & New Deaths \n‌ ",
                        inline=False)

        embed.add_field(name="> c;help",
                        value="The 'help' command will display a embed containing help formation about the bot\n‌ ",
                        inline=False)

        embed.add_field(name="> Support & Feedback",
                        value="If you have found an issue / bug related to the bot or would like to provide feedback you can by joining our discord `https://discord.gg/7TqeUHE` or adding and dming me on discord @`Ｃｏｄｙ#7144`\n‌ ",
                        inline=False)

        await message.channel.send(
            content="‌‌ \n**`COVID Watch Help Article`**\n*`Our bot contains many features for easily indexing the content you want`*\n*`The bots prefix is simply:`*` `***`c;`***",
            embed=embed)