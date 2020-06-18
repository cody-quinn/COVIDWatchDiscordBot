import discord, datetime, random, time
from bot.commands.command import Command


class AdviceCMD(Command):
    async def run(self, message, raw_args):
        allInfo = False

        args = []
        for rarg in raw_args.split('-'):
            arg = rarg.split(' ')
            for i in arg:
                if i == '':
                    arg.remove('')
            if len(arg) > 0:
                args.append(arg)

        for arg in args:
            if len(arg) < 1:
                continue
            if arg[0] == "all" or arg[0] == "a":
                allInfo = True

        embed = discord.Embed(colour=discord.Colour(0x1d837e), timestamp=time.time())

        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")
        embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                         icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

        advices = ['Make sure to **wear a mask** in public', 'Try to avoid contact with people!',
                   'Dont visit your elders; you could get them sick!',
                   'Seniors, People with medical issues, or infants are at higher risk',
                   'Stay 6 feet apart from the public',
                   'Remember that you can make it through the pandemic',
                   'Dont freak out. Staying calm and following the rules helps',
                   'Covid cannot spread through mosquito, flea, or tick bites',
                   'Always wash your hands after going out.',
                   'Being healthy doesnt necessarily mean you are immune to covid.',
                   'Feel free to call people you know; They probably need attention as much as you do!',
                   'Covid will pass. There is no need to freak out about it',
                   'Fight back by staying inside!']
        final_advice = ""
        if allInfo:
            i = 0
            for adv in advices:
                i += 1
                final_advice = final_advice + "**`" + str(i) + "-`**" + adv + "\n"
        else:
            for i in range(3):
                while True:
                    ii = random.randint(0, len(advices) - 1)
                    if not advices[ii] in final_advice:
                        final_advice = final_advice + "**`" + str(i + 1) + "-`**" + advices[ii] + "\n"
                        break

        embed.add_field(name="Advice", value=final_advice)

        await message.channel.send(content="‌‌ \n**`Coronavirus Advice`**\n*`Please stay safe`*", embed=embed)
