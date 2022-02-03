class BouncyBallCommand: 
    led = None
    bg = None
    ball = None
    gradient = None
    curr = None
    r = None
    diff = 1
    numSections = None

    def __init__(self, led, bg, ball, r):
        self.led = led
        self.bg = bg
        self.ball = ball
        self.r = r
        self.curr = r

        increments = [(bg.r - ball.r) / r, (bg.g - ball.g) / r, (bg.b - ball.b) / r]

        self.numSections = 2 * r + 1
        self.gradient = [0] * self.numSections
        for i in range(self.numSections): 
            dist = abs(i - int(self.numSections / 2.0))
            self.gradient[i] = (ball.r + increments[0] * dist, ball.g + increments[1] * dist, ball.b + increments[2] * dist)


    def execute(self): 
        for i in range(0, self.led.getBufferLength()):
            if i >= self.curr - self.r and i <= self.curr + self.r:
                mid = int(((self.curr + self.r) + (self.curr - self.r)) / 2.0)
                dist = i - mid + int(self.numSections / 2.0)
                self.led.setRGB(i, self.gradient[dist][0], self.gradient[dist][1], self.gradient[dist][2])
            else: 
                self.led.setRGB(i, self.bg.r, self.bg.g, self.bg.b)
        self.curr += self.diff

        if self.curr == self.led.getBufferLength() - self.r - 1 or self.curr == self.r: 
            self.diff *= -1

        self.led.sendData()
    
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led