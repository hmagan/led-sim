class RainbowCommand: 
    led = None
    rainbowPixelFirstHue = None

    def __init__(self, led, rainbowPixelFirstHue):
        self.led = led
        self.rainbowPixelFirstHue = rainbowPixelFirstHue

    def execute(self): 
        for i in range(self.led.getBufferLength()):
            hue = (self.rainbowPixelFirstHue + (i * 180 / self.led.getBufferLength())) % 180
            self.led.setHSV(i, hue, 255, 128)
        self.rainbowPixelFirstHue += 3
        self.rainbowPixelFirstHue %= 180
        self.led.sendData()
    
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led