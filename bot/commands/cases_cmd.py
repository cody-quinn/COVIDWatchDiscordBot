import discord, datetime
from bot.commands.command import Command
from bot import get_data


class CasesCMD(Command):
    async def run(self, message, raw_args):
        scope = "global"
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
            if arg[0] == "country" or arg[0] == "c":
                if len(arg) > 1:
                    scope = ""
                    for scopeArg in arg[1:]:
                        scope = scope + str(scopeArg)
                        if scopeArg != arg[len(arg)-1]:
                            scope = scope + " "

                    # Adding special cases to countries that should have them
                    if scope.lower() == "usa" or scope.lower() == "united states":
                        scope = "US"
                else:
                    await message.channel.send("**`You must enter the name of a country you would like to scope into.`**")
            if arg[0] == "all" or arg[0] == "a":
                allInfo = True
            # if arg[0] == "day":
            #     ##TODO: Add date selector

        data = get_data()
        if 199 < data['Status'] < 300: #Im afraid the country you selected could not be found, maybe there was a spelling mistake?
            embed = discord.Embed(colour=discord.Colour(0x9c0519), timestamp=datetime.datetime.utcfromtimestamp(1589100774))
            embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                             icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

            if scope.lower() == "global":
                res_g = data['Result']['Global']['Global']

                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/International_Flag_of_Planet_Earth.svg/800px-International_Flag_of_Planet_Earth.svg.png")

                death_rate = str(int(str(res_g['TotalDeaths']).replace(',','')) / int(str(res_g['TotalConfirmed']).replace(',','')) * 100)
                death_rate = death_rate[:6] + "%"
                active_cases = str(res_g['TotalConfirmed'] - res_g['TotalDeaths'] - res_g['TotalRecovered'])

                embed.add_field(name="Currently Infected", value='{:,}'.format(int(active_cases)), inline=False)
                embed.add_field(name="Total Recovered", value='{:,}'.format(int(res_g['TotalRecovered'])), inline=False)
                embed.add_field(name="Total Deaths", value='{:,}'.format(int(res_g['TotalDeaths'])), inline=False)
                embed.add_field(name="Total Cases", value='{:,}'.format(int(res_g['TotalConfirmed'])))
                embed.add_field(name="Death Rate", value=death_rate)

                if allInfo:
                    embed.add_field(name="Cases Per Million", value="Coming Soon")
                    embed.add_field(name="New Cases", value='{:,}'.format(int(res_g['NewConfirmed'])))
                    embed.add_field(name="New Deaths", value='{:,}'.format(int(res_g['NewDeaths'])))
                    embed.add_field(name="New Recovered", value='{:,}'.format(int(res_g['NewRecovered'])))
            else:
                for country in data['Result']['Global']['Countries']:
                    if country['Country'].lower() == scope.lower() or country['CountryCode'].lower() == scope.lower() or country['Slug'] == scope.lower():
                        embed.set_thumbnail(url="https://www.countryflags.io/"+country['CountryCode'].lower()+"/flat/64.png")

                        death_rate = str(int(str(country['TotalDeaths']).replace(',','')) / int(str(country['TotalConfirmed']).replace(',','')) * 100)
                        death_rate = death_rate[:6] + "%"
                        active_cases = str(country['TotalConfirmed'] - country['TotalDeaths'] - country['TotalRecovered'])

                        embed.add_field(name="Currently Infected", value='{:,}'.format(int(active_cases)), inline=False)
                        embed.add_field(name="Total Recovered", value='{:,}'.format(int(country['TotalRecovered'])), inline=False)
                        embed.add_field(name="Total Deaths", value='{:,}'.format(int(country['TotalDeaths'])), inline=False)
                        embed.add_field(name="Total Cases", value='{:,}'.format(int(country['TotalConfirmed'])))
                        embed.add_field(name="Death Rate", value=death_rate)

                        if allInfo:
                            embed.add_field(name="Cases Per Million", value="Coming Soon")
                            embed.add_field(name="New Cases", value='{:,}'.format(int(country['NewConfirmed'])))
                            embed.add_field(name="New Deaths", value='{:,}'.format(int(country['NewDeaths'])))
                            embed.add_field(name="New Recovered", value='{:,}'.format(int(country['NewRecovered'])))

            await message.channel.send(content="‌‌ \n**`Coronavirus Statistics for "+scope+"`**\n*`Last Update: "+str(data['Result']['Global']['Countries'][0]['Date'])+"`*", embed=embed)
        else:
            await message.channel.send("**`Covid api returned status code {}. Please wait a minute then rerun this command as these issues usually fix themselves.`**".format(data['Status']))