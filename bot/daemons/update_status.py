import discord, threading, asyncio, requests, time
from daemons.update_data import UpdateData


class UpdateStatus(object):
    def __init__(self, client):
        self.client = client
        self.covidData = UpdateData()

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        state=1
        while True:
            time.sleep(4)

            if state==1:
                state=2
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Deaths'.format(int(self.covidData.results['Global']['TotalDeaths']))))
                    except:
                        print("Exception settings status")
                asyncio.run(update())
            elif state == 2:
                state = 3
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Recoveries'.format(int(self.covidData.results['Global']['TotalRecovered']))))
                    except:
                        print("Exception setting status")
                asyncio.run(update())
            elif state == 3:
                state = 4
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Casses'.format(int(self.covidData.results['Global']['TotalConfirmed']))))
                    except:
                        print("Exception setting status")
                asyncio.run(update())
            elif state == 4:
                state = 5
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Activity(name="c;help", type=discord.ActivityType.listening))
                    except:
                        print("Exception setting status")
                asyncio.run(update())
            elif state == 5:
                state = 1
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Activity(name="{} servers".format(len(self.client.guilds)), type=discord.ActivityType.watching))
                    except:
                        print("Exception setting status")
                asyncio.run(update())