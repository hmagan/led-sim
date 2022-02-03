class CommandScheduler:
    commands = []

    def __init__(self):
        pass

    def addCommand(self, command):
        self.commands.append(command)

    def removeCommand(self, led):
        for command in self.commands:
            if command.getLED() == led: 
                self.commands.remove(command)

    def update(self):
        for command in self.commands: 
            command.execute()
            if command.isFinished():
                command.end()
                self.commands.remove(command)
