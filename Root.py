from tkinter import *

from matplotlib.colors import rgb2hex
from Constants import *
from math import sqrt, atan2, pi

class Root(Tk):
    objects = []
    ledObjs = []
    canvas = None
    cs = None
    fw = None

    def __init__(self, leds, cs, fw):
        super(Root, self).__init__()
        self.title("LED Testing")
        self.minsize(WIDTH, HEIGHT)
        self.resizable(False, False)

        # Create canvas
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill="both", expand=True)
        
        # Display background (field) image
        # bg = PhotoImage(file="./assets/field_2020.png")
        # self.canvas.create_image(0, 0, image=bg, anchor="nw")
        # self.canvas.image = bg

        self.canvas.configure(bg="black", highlightthickness=0)

        for led in leds: 
            self.ledObjs.append(led)

        self.cs = cs
        self.fw = fw
        
    def resetPoints(self): 
        if len(self.points) > 2: 
            del self.points[1:len(self.points)-1]

    def toRad(self, deg): 
        return deg * pi / 180

    def toDeg(self, rad): 
        return rad * 180 / pi

    def angleDiff(self, a, b): 
        angle = a - b
        return (angle + 180.0) % 360.0 - 180.0

    def drawCircle(self, x, y, r, fill="#ffbb00"): 
        self.objects.append(self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=fill))

    def drawLine(self, x0, y0, x1, y1): 
        self.objects.append(self.canvas.create_line(x0, y0, x1, y1))

    def drawText(self, x, y, txt, fill="#ffffff"): 
        self.objects.append(self.canvas.create_text(x, y, text=txt, fill=fill))

    def drawRectangle(self, x0, y0, x1, y1, color): 
        self.objects.append(self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=""))

    def clearObjects(self): 
        for obj in self.objects: 
            self.canvas.delete(obj)
        self.objects.clear()

    def calcDiff(self, x0, y0, x1, y1): # 0 = curr, 1 = prev
        xdiff = self.pixWidthToInches(x0 - x1)
        ydiff = self.pixHeightToInches(y0 - y1)
        mag = sqrt(xdiff * xdiff + ydiff * ydiff)
        angle = self.toDeg(abs(atan2(ydiff, xdiff)))
        if y1 < y0: 
            angle = 180.0 + (180.0 - angle)
        return mag, angle

    def rgb2hex(self, rgb):
        return '%02x%02x%02x' % rgb
    
    def updateLEDS(self): 
        self.cs.update()

    def drawLEDS(self): 
        self.clearObjects()

        y = 250
        width = 7
        height = 50 # height of each node
        dist = 200 # distance between LEDs

        for led in self.ledObjs: 
            strip = led.getStrip()
            x = 10
            for node in strip: 
                self.drawRectangle(x, y, x + width, y + height, rgb2hex((node.r / 255.0, node.g / 255.0, node.b / 255.0)))
                x += width
            y += dist
        
        # self.drawText(1025, 35, "RPM: " + str(self.fw.getRPM()))
        # self.drawText(1025, 15, "setPoint: " + str(5000))