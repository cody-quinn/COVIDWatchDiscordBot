#Imports
import discord
from bot.commands.command import Command


registered_commands = []
client = discord.Client()


def main():
    registered_commands.append(Command("hello"))

    @client.event
    async def on_message(message):
        command = ""
        args_raw = ""
        split_raw = []
        split_args = []

        if ' ' in message.content:
            split_raw = str(message.content).split(' ')
            for i in range(len(split_raw)):
                if '' in split_raw:
                    split_raw.remove('')
        else:
            split_raw = [message.content]
        split_args = args_raw.split('-')

        if 'c;' in split_raw[0][0:2].lower():
            if "c;" in split_raw[0][0:2].lower():
                command = str(split_raw[0]).lower().replace("c;", "")
            split_raw.pop(0)

            for s in split_raw:
                args_raw = args_raw + s + " "
            print(args_raw)

            for cmd in registered_commands:
                if cmd.command == command:
                    args = []
                    for a in split_args:
                        b = a.split(' ')
                        c = {'name': b[0]}
                        b.pop(0)
                        for e in b:
                            c['value'] = c['value'] + e
                        args.append(c)
                    await cmd.run(message, args)

    client.run('NzA5MTI2MTI3MDAzNzYyODA4.Xr9SGQ.kwpFBCK2-0ijLhGklMvXadUZbQA')


if __name__ == "__main__":
    main()