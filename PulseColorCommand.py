import colorsys

class PulseColorCommand: 
    led = None
    color = None
    currL = 1
    maxV = 0
    diff = 1

    def __init__(self, led, color):
        self.led = led
        self.color = colorsys.rgb_to_hsv(color.r / 255.0, color.g / 255.0, color.b / 255.0)
        self.maxV = self.color[2]

    def execute(self): 
        for i in range(self.led.getBufferLength()):
            self.led.setHSV(i, self.color[0] * 360.0, self.color[1] * 255.0, self.currL)
        self.led.sendData()

        self.currL += self.diff

        if self.currL == 128 or self.currL == 1:
            self.diff *= -1
        
        
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led