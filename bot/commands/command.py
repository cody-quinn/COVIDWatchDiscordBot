class Command:
    def __init__(self, command):
        self.command = str(command)
        self.init()

    async def run(self, message, raw_args):
        args = []
        for rarg in raw_args.split('-'):
            arg = rarg.split(' ')
            for i in arg:
                if i == '':
                    arg.remove('')
            if len(arg > 0):
                args.append(arg)

        for arg in args:
           await message.channel.send("{}".format(str(arg)))

    def init(self):
        pass