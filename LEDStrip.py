import colorsys
from Color import Color
from Constants import YETI_BLUE

class LEDStrip(): 
    length = 0
    buffer = []
    strip = []

    def __init__(self, length):
        self.length = length
        self.strip = [YETI_BLUE] * length
        self.buffer = [YETI_BLUE] * length

    def setRGB(self, idx, r, g, b): 
        self.buffer[idx] = Color(r, g, b)
    
    def setHSV(self, idx, h, s, v): 
        c = self.hsv2rgb(h, s, v)
        self.buffer[idx] = Color(c[0], c[1], c[2])

    def getBufferLength(self): 
        return self.length

    def sendData(self): 
        self.strip = self.buffer

    def getStrip(self): 
        return self.strip

    def hsv2rgb(self, h, s, v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h / 360.0, s / 255.0, v / 128.0))