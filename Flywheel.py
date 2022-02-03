class Flywheel: 
    rpm = 0
    maxRPM = 5000

    def __init__(self):
        pass

    def increasRPM(self, inc): 
        self.rpm += inc
        if self.rpm > self.maxRPM: 
            self.rpm = self.maxRPM

    def decreaseRPM(self, dec): 
        self.rpm -= dec
        if self.rpm < 0: 
            self.rpm = 0

    def getRPM(self):
        return self.rpm

    def stopFlywheel(self): 
        self.rpm = 0 # obv wouldnt work like this but just for demo purposes