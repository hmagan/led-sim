class EpilepsyCommand: 
    led = None
    idx = 0
    colors = [
        (77, 173, 75), # greenish
        (21, 216, 237), # light blue
        (171, 101, 221), # purple
        (250, 77, 127), # pink
    ]

    def __init__(self, led):
        self.led = led

    def execute(self): 
        for i in range(self.led.getBufferLength()):
            self.led.setRGB(i, self.colors[self.idx][0], self.colors[self.idx][1], self.colors[self.idx][2])
        self.idx += 1
        self.idx %= len(self.colors)
        self.led.sendData()
        
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led