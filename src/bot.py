import discord, requests, time, threading, asyncio, datetime


current_milli_time = lambda: int(round(time.time() * 1000))
update_channels = []
client = discord.Client()


def get_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = get_token()


def get_client_id():
    with open("clientid.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
client_id = get_client_id()


def main():
    @client.event
    async def on_message(message):
        command = ""
        args_raw = ""
        ran = False
        split_raw = []

        if ' ' in message.content:
            split_raw = str(message.content).split(' ')
            for i in range(len(split_raw)):
                if '' in split_raw:
                    split_raw.remove('')
        else:
            split_raw = [message.content]

        if "<@!" + client_id + ">" in split_raw[0] or 'c;' in split_raw[0][0:2].lower():
            if "<@!" + client_id + ">" in split_raw[0]:
                command = str(split_raw[1]).lower()
                split_raw.pop(0)
            elif "c;" in split_raw[0][0:2].lower():
                command = str(split_raw[0]).lower().replace("c;", "")
            split_raw.pop(0)

            for s in split_raw:
                args_raw = args_raw + s + " "

            scope = "World"
            setting = ""
            all_info = False


            # Setting Arguments
            if "-" in str(args_raw).lower():  # Checking to see if there are any arguments
                args = str(args_raw).split("-")  # Splitting up all the arguments
                args.remove('')  # Popping anything with nothing in it

                for arg in args:
                    sub_args = arg.split(" ")

                    if sub_args[0] == 'country' or sub_args[0] == 'location' and len(sub_args) > 1:  # Setting the country argument
                        resp = requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search')

                        if resp.status_code != 200:
                            await message.channel.send("Error! Unexpected response code " + str(
                                resp.status_code) + ". Please do not report this unless it goes on for a while as its mostlikely not an issue related to us.")
                        else:
                            for country in resp.json()['data']['rows']:
                                if str(country['country']).lower() == str(sub_args[1]).lower() or str(country['country_abbreviation']).lower() == str(sub_args[1]).lower():
                                    scope = str(country['country'])
                                elif scope=="World":
                                    scope = "null"

                    if sub_args[0] == 'a' or sub_args[0] == 'all' or sub_args[0] == 'more':
                        all_info = True

                    if sub_args[0] == 'update_channel':
                        setting = 'update_channel'


            # Getting Command Executed and executing
            if command == "cases" or command == "info" or command == "data":
                ran=True

                resp = requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/countries-search')
                embed = discord.Embed(colour=discord.Colour(0x9c0519), timestamp=datetime.datetime.utcfromtimestamp(1589100774))

                for item in resp.json()['data']['rows']:
                    if item['country'] == scope:
                        embed.set_thumbnail(url=item['flag'])
                        embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                                         icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

                        embed.add_field(name="Currently Infected", value=item['active_cases'], inline=False)
                        embed.add_field(name="Total Recovered", value=item['total_recovered'], inline=False)
                        embed.add_field(name="Total Deaths", value=item['total_deaths'], inline=False)
                        embed.add_field(name="Total Cases", value=item['total_cases'])
                        embed.add_field(name="Cases Per Million", value=item['cases_per_mill_pop'])
                        embed.add_field(name="Death Rate", value="Feature Coming Soon")

                        if all_info:
                            embed.add_field(name="New Cases", value=item['new_cases'])
                            embed.add_field(name="New Deaths", value=item['new_deaths'])
                            embed.add_field(name="Serious Critical", value=item['serious_critical'])

                if scope == 'null':
                    countries_list = ""
                    for item in resp.json()['data']['rows']:
                        countries_list = countries_list + item['country'] + "  -  " + item['country_abbreviation'] + "\n"
                    await message.channel.send(
                        content="‌‌ \n**`Country selected not found, here is a list of countries in our index`** ```yaml\n"+countries_list+"```")
                else:
                    await message.channel.send(content="‌‌ \n**`Coronavirus Statistics for "+scope+"`**\n*`Last Update: "+str(resp.json()['data']['last_update'])+"`*", embed=embed)

            if command == "symptoms":
                ran=True

                embed = discord.Embed(colour=discord.Colour(0x1d837e), timestamp=datetime.datetime.utcfromtimestamp(1589104767))

                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")
                embed.set_footer(text="Covid Watch - Coronavirus Statistics", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

                embed.add_field(name="Information", value='''
                    COVID19 is a deadly virus that rapidly spreads and kills, here are the symptoms of the virus, if you experience one or many of these symptoms please get tested and seek medical advice. A very worrying part of COVID19 is that it takes up to 2 weeks before you have symptoms if you experience any at all
                ''', inline=False)
                embed.add_field(name="Symptoms", value='''
                **`1-`** A Cough\n**`2-`** Shortness in breath\n**`3-`** Fever\n**`4-`** Chills\n**`5-`** Repeated shaking with chills\n**`6-`** Muscle Pain\n**`7-`** Headache\n**`8-`** Sore throat\n**`9-`** Trouble breathing\n**`10-`** Persistent pain or pressure in the chest\n**`11-`** New confusion or inability to arouse\n**`12-`** Bluish lips or face
                ''')

                await message.channel.send(content="‌‌ \n**`Coronavirus Symptoms`**\n*`Please stay safe`*", embed=embed)

            if command == "settings" or command == "s":
                ran=True

                message = await message.channel.send(
                    "This command is almost done!")
                time.sleep(4)
                await message.delete()

            if command == "help" or command == "h":
                ran=True

                embed = discord.Embed(colour=discord.Colour(0x1d837e),
                                      timestamp=datetime.datetime.utcfromtimestamp(1589104767))

                embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Question_mark_(black).svg/1200px-Question_mark_(black).svg.png")
                embed.set_footer(text="Covid Watch - Coronavirus Statistics",
                                 icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/SARS-CoV-2_without_background.png/220px-SARS-CoV-2_without_background.png")

                embed.add_field(name="> c;cases",
                                value="The 'cases' command will display a embed containing updated information about all the cases worldwide or in a selected region \n\n __**Modifiers**__\n     ***__`-country <target>`__***  -  Targets a specific country\n     ***__`-all`__***  -  Displays extra data, such as 'new' cases & 'new' deaths\n\n__**Example**__\n     **`c;cases -country USA -all`**  -  Will target the USA and display all information including New Cases & New Deaths \n‌ ",
                                inline=False)
                embed.add_field(name="> c;symptoms",
                                value="The 'symptoms' command will display symptoms and information about the coronavirus\n‌ ",
                                inline=False)
                # embed.add_field(name="> c;settings",
                #                 value="The 'settings' command will allow you to change various settings related to the bot \n\n __**Modifiers (settings)**__\n     ***__`-update_channel`__***  -  Sets the message your messaging from to a update channel\n‌ ",
                #                 inline=False)
                embed.add_field(name="> c;help",
                                value="The 'help' command will display a embed containing help formation about the bot\n‌ ",
                                inline=False)

                await message.channel.send(
                    content="‌‌ \n**`COVID Watch Help Article`**\n*`Our bot contains many features for easily indexing the content you want`*\n*`The bots prefix is simply mentioning (@ing) it before the command`*",
                    embed=embed)

            if ran == False:
                await message.channel.send(content="Did you mean *`c;help`* ?")

    bla = updateStatus(client)
    bla.start()

    client.run(token)


class updateStatus(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.running = True
        self.client = client

    def run(self):
        state = 1

        while self.open():
            time.sleep(4)

            resp = requests.get('https://corona-virus-stats.herokuapp.com/api/v1/cases/general-stats')

            if state==1:
                state=2
                async def update():
                    await self.client.change_presence(
                        activity=discord.Game(name=resp.json()['data']['death_cases'] + " Deaths"))
                asyncio.run(update())
            elif state == 2:
                state = 3
                async def update():
                    await self.client.change_presence(
                        activity=discord.Game(name=resp.json()['data']['total_cases'] + " Total Cases"))
                asyncio.run(update())
            elif state == 3:
                state = 4
                async def update():
                    await self.client.change_presence(
                        activity=discord.Game(name=resp.json()['data']['currently_infected'] + " Infected"))
                asyncio.run(update())
            elif state == 4:
                state = 5
                async def update():
                    await self.client.change_presence(
                        activity=discord.Game(name=resp.json()['data']['recovery_cases'] + " Recoveries"))
                asyncio.run(update())
            elif state == 5:
                state = 1
                async def update():
                    await self.client.change_presence(
                        activity=discord.Game(name="c;help"))
                asyncio.run(update())


        print("Thread Closed")

    def open(self):
        return self.running

    def close(self):
        self.running = False


if __name__ == "__main__":
    main()