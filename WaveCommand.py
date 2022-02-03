import colorsys

from Color import Color

class WaveCommand: 
    led = None
    firstColor = None
    secondColor = None
    colorQueue = None

    def __init__(self, led, firstColor, secondColor):
        self.led = led

        initialState = [None] * led.getBufferLength()
        currRGB = [firstColor.r, firstColor.g, firstColor.b]

        # Generate the initial state of the LED strip so colorQueue can easily shift the colors down by 1 
        # each time to create a motion effect. Instead of making a gradient from firstColor -> secondColor, 
        # make one from firstColor -> secondColor -> firstColor so the gradient looks smooth after pushing
        # on the queue.

        end = int(led.getBufferLength() / 2 if led.getBufferLength() % 2 == 0 else led.getBufferLength() / 2 + 1)
        increments = [(secondColor.r - firstColor.r) / end, (secondColor.g - firstColor.g) / end, (secondColor.b - firstColor.b) / end]

        for i in range(0, end):
            initialState[i] = Color(currRGB[0], currRGB[1], currRGB[2])
            for j in range(0, len(currRGB)):
                currRGB[j] += increments[j]

        idx = int(led.getBufferLength() / 2 - 1)
        for i in range(end, led.getBufferLength()): 
            initialState[i] = Color(initialState[idx].r, initialState[idx].g, initialState[idx].b)
            idx -= 1

        self.colorQueue = initialState

    def execute(self): 
        for i in range(self.led.getBufferLength()):
            self.led.setRGB(i, self.colorQueue[i].r, self.colorQueue[i].g, self.colorQueue[i].b)
        self.colorQueue.append(self.colorQueue.pop(0))
        self.led.sendData()
        
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led