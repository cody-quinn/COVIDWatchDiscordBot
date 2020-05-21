import discord, threading, asyncio, requests, time

class UpdateStatus(object):
    def __init__(self, client):
        self.client = client

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        state=1
        while True:
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