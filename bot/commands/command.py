import discord

class Command:
    def __init__(self, command):
        self.command = str(command)


    async def run(self, message, **args):
        await message.channel.send("Hello World!")

        for arg in args['args']:
            arg = dict(arg)