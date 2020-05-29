import dbl, asyncio
from bot import log, getPreferences
from discord.ext import tasks


class UpdateTopGG(object):
    def __init__(self, client):
        self.client = client
        if len(getPreferences()['dbl_token']) > 0:
            self.dbl_token = getPreferences()['dbl_token']
            self.dbl_interface = dbl.DBLClient(self.client, self.dbl_token)
        else:
            log("No DBL token found, not updating bot page")

    @tasks.loop(minutes=10.0)
    async def update(self):
        try:
            await self.dbl_interface.post_guild_count()
            log("Posted server count to DBL ({})".format(self.dbl_interface.guild_count()))
        except Exception as e:
            log("Failed to update DBL \n Stacktrace: {}".format(e))
        await asyncio.sleep(600)