import discord
from bot.commands.command import Command

class CasesCMD(Command):
    async def run(self, message, raw_args):
        scope = "global"
        allInfo = False

        args = []
        for rarg in raw_args.split('-'):
            arg = rarg.split(' ')
            for i in arg:
                if i == '':
                    arg.remove('')
            if len(arg > 0):
                args.append(arg)

        for arg in args:
            if len(arg) < 1:
                continue
            if arg[0] == "country" or arg[0] == "c":
                if len(arg) > 1:
                    scope = arg[1]
                else:
                    ##TODO: Add callback
            if arg[0] == "all" or arg[0] == "a":
                allInfo = True
            if arg[0] == "day":
                ##TODO: Add day selector


