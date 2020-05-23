#Imports
import discord, requests, threading, asyncio, time
from bot.commands import CasesCMD, HelpCMD
from bot.daemons import UpdateStatus

registered_commands = []


def main():
    client = discord.Client()
    registered_commands.append(CasesCMD("cases"))
    registered_commands.append(HelpCMD("help"))

    @client.event
    async def on_message(message):
        if ' ' in message.content:
            split_msg = str(message.content).split(' ')
            for i in range(len(split_msg)):
                if '' in split_msg:
                    split_msg.remove('')
        else:
            split_msg = [message.content]

        if 'c;' == split_msg[0][0:2].lower():
            command = str(split_msg[0][2:])
            args = ""
            for a in split_msg[1:]:
                args += a + " "

            ran = False
            for cmd in registered_commands:
                if cmd.command == command:
                    await cmd.run(message, args)
            if not ran:
                await message.channel.send(content="Did you mean *`c;help`* ?")

    @client.event
    async def on_ready():
        UpdateStatus(client)
    client.run('NzA5MTI2MTI3MDAzNzYyODA4.Xr9SGQ.kwpFBCK2-0ijLhGklMvXadUZbQA')


if __name__ == "__main__":
    main()
