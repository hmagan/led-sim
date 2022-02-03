class FlywheelCommand: 
    led = None
    fw = None
    setpoint = 5000
    tolerance = 100
    green = [0, 255, 38]
    red = [255, 0, 0]
    gradient = None

    def __init__(self, led, fw):
        self.led = led
        self.fw = fw
        self.gradient = self.makeGradient(self.green, self.red, 4000)


    def execute(self): 
        rpm = self.fw.getRPM()
        if rpm > self.setpoint: 
            rpm = self.setpoint - (rpm - self.setpoint)
        rgb = self.gradient[rpm-1 - 1000] if rpm > 1000 else self.red
        for i in range(self.led.getBufferLength()):
            self.led.setRGB(i, rgb[0], rgb[1], rgb[2])

        self.led.sendData()
    
    def end(self): 
        pass

    def isFinished(self):
        return False

    def getLED(self):
        return self.led

    def makeGradient(self, f, s, n):
        RGB_list = [s]
        for t in range(1, n):
            curr_vector = [
                int(s[j] + (float(t)/(n-1))*(f[j]-s[j]))
                for j in range(3)
            ]
            RGB_list.append(curr_vector)
        return RGB_list