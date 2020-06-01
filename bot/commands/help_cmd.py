import discord, datetime
from bot.commands.command import Command


class HelpCMD(Command):
    async def run(self, message, raw_args):
        embed = discord.Embed(
            title=":grey_question: __COVIDWatch Help__",
            description="For a more extensive help page please visit [here](https://github.com/CatDevz/COVIDWatchDiscordBot). If you are seeking support you can join our [discord server](https://discord.gg/7TqeUHE). If you would like to contribute or read the code here is our [github](https://github.com/CatDevz/COVIDWatchDiscordBot). Please [vote](https://top.gg/bot/708929935443492995) for our bot on top.gg and [click here](https://discord.com/api/oauth2/authorize?client_id=708929935443492995&permissions=67584&scope=bot) if you would like to add this bot to your server.\n‌ ",
            colour=discord.Colour(0x9c0519),
            # timestamp=datetime.datetime.utcfromtimestamp(1589100774)
        )
        embed.set_footer(text="Covid Watch - Coronavirus Statistics • Version 1.1")

        embed.add_field(name="**__Commands__**",
                        value="• `c;cases` - Check the current amount of cases globally \n• `c;cases -country {country}` - Check the current amount of cases in a specific country \n• `c;advice` - View advice about covid \n• `c;symptoms` - View symptoms of covid \n• `c;help` - Help related to the bot \n‌ ",
                        inline=False)

        embed.add_field(name="**__Features__**",
                       value="• Multiple commands for easy viewing of latest statistics \n• Statistics from [covid19api](https://covid19api.com/) \n• Statistics shown on the bots status \n‌ ",
                       inline=False)

        await message.channel.send(embed=embed)