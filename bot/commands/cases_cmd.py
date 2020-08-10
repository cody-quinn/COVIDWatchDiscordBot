import discord, datetime, requests, time
from bot.commands.command import Command
from bot.daemons.update_data import UpdateData


class CasesCMD(Command):
    async def run(self, message, raw_args):
        scope = "global"

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
                    if scope.lower() == "uk":
                        scope = "United Kingdom"
                    if scope.lower() == "aus":
                        scope = "Australia"
                else:
                    await message.channel.send("**`You must enter the name of a country you would like to scope into.`**")

        if self.covidData.req:
            if scope.lower() == "global":
                res_g = self.covidData.results['Global']
                title = "COVID19 Cases Globally"
            else:
                for country in self.covidData.results['Countries']:
                    if country['Country'].lower() == scope.lower() or country['CountryCode'].lower() == scope.lower() or country['Slug'] == scope.lower():
                        res_g = country
                        title = "COVID19 Cases | :flag_{}:".format(country['CountryCode'].lower())
                        break

            try:
                embed = discord.Embed(
                    title=title,
                    description="Please **[vote](https://top.gg/bot/708929935443492995)** for my bot on **top.gg** | All data from **[covid19api](https://covid19api.com/)** \nStatistics last updated **{} GMT**".format(str(datetime.datetime.fromisoformat(self.covidData.results['Countries'][0]['Date'][:19]))),
                    colour=discord.Colour(0x9c0519),
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                                 icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

                death_rate = str(int(str(res_g['TotalDeaths']).replace(',', '')) / int(
                    str(res_g['TotalConfirmed']).replace(',', '')) * 100)
                death_rate = death_rate[:6] + "%"
                active_cases = res_g['TotalConfirmed'] - res_g['TotalDeaths'] - res_g['TotalRecovered']

                cpm = "Error getting cpm"
                if not scope.lower() == 'global':
                    wd_req = requests.get("https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-population%40kapsarc&rows=1&sort=year&refine.country_name={}".format(res_g['Country']))
                    if 199 < wd_req.status_code < 300:
                        for wd_country in wd_req.json()['records']:
                            if wd_country['fields']['country_name'] == res_g['Country']:
                                cpm = str(active_cases / wd_country['fields']['value'])
                                break

                embed.add_field(name=":biohazard: Confirmed Cases",
                                value='**{:,}** (+{:,})'.format(res_g['TotalConfirmed'], res_g['NewConfirmed']))
                embed.add_field(name=":heart: Recovered",
                                value='**{:,}** (+{:,})'.format(res_g['TotalRecovered'], res_g['NewRecovered']))
                embed.add_field(name=":skull_crossbones: Deaths",
                                value='**{:,}** (+{:,})'.format(res_g['TotalDeaths'], res_g['NewDeaths']))
                embed.add_field(name=":nauseated_face: Active Cases",
                                value='**{:,}**'.format(active_cases))
                embed.add_field(name=":grey_exclamation: Death Rate",
                                value='**{}**'.format(death_rate))
                embed.add_field(name=":grey_exclamation: Cases Per Million",
                                value='**{}**'.format(cpm[:6]))
                await message.channel.send(embed=embed)
            except UnboundLocalError:
                embed = discord.Embed(
                    title="COVIDWatch Error",
                    description="Were sorry however we could not find a country under **{}** inside our database. Maybe try using its full name or another alias, and make sure you spelt it correctly. You can find a list of all supported countries **[here](https://api.covid19api.com/summary)**".format(scope),
                    colour=discord.Colour(0x9c0519),
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                                 icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

                await message.channel.send(embed=embed)
        else:
            await message.channel.send("**`Covid api returned status code {}. Please wait a minute then rerun this command as these issues usually fix themselves.`**".format(self.covidData.unstable_req.status_code))

    def init(self):
        self.covidData = UpdateData()
