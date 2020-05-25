import discord, threading, asyncio, time
from bot import log, get_data


class UpdateStatus(object):
    def __init__(self, client):
        self.client = client

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        log("Update Status daemon started.")

        state=5
        while True:
            try:
                if state >= 5:
                    data = get_data()['Result']['Global']['Global']
            except:
                log("Failed to get data for status update.")

            if state==1:
                state=2
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Deaths'.format(int(data['TotalDeaths']))))
                    except:
                        log("Failed to update bot status")
                asyncio.run(update())
            elif state == 2:
                state = 3
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Recoveries'.format(int(data['TotalRecovered']))))
                    except:
                        log("Failed to update bot status")
                asyncio.run(update())
            elif state == 3:
                state = 4
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Game(name='{:,} Casses'.format(int(data['TotalConfirmed']))))
                    except:
                        log("Failed to update bot status")
                asyncio.run(update())
            elif state == 4:
                state = 5
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Activity(name="c;help", type=discord.ActivityType.listening))
                    except:
                        log("Failed to update bot status")
                asyncio.run(update())
            elif state == 5:
                state = 1
                async def update():
                    try:
                        await self.client.change_presence(activity=discord.Activity(name="{} servers".format(len(self.client.guilds)), type=discord.ActivityType.watching))
                    except:
                        log("Failed to update bot status")
                asyncio.run(update())
            time.sleep(4)