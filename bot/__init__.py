#Imports
import discord
from bot.commands.command import Command

registered_commands = []
client = discord.Client()

'''
    {
        args: [
            {key: x, value: y}
            {key: x, value: y}
            {key: x, value: y}
        ]
    }
'''


def main():
    registered_commands.append(Command("hello"))

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

            for cmd in registered_commands:
                if cmd.command == command:
                    await cmd.run(message)

    client.run('NzA5MTI2MTI3MDAzNzYyODA4.Xr9SGQ.kwpFBCK2-0ijLhGklMvXadUZbQA')


if __name__ == "__main__":
    main()