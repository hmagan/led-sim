from BouncyBallCommand import BouncyBallCommand
from AuroraCenterInCommand import AuroraCenterInCommand
from AuroraCenterOutCommand import AuroraCenterOutCommand
from Color import Color
from CommandScheduler import CommandScheduler
from Constants import YETI_BLUE
from EpilepsyCommand import EpilepsyCommand
from Flywheel import Flywheel
from FlywheelCommand import FlywheelCommand
from LEDStrip import LEDStrip
from PulseColorCommand import PulseColorCommand
from RainbowCommand import RainbowCommand
from Root import Root
from WaveCommand import WaveCommand

flywheel = Flywheel()

def handleUpKey(e): 
    flywheel.increasRPM(50)

def handleDownKey(e):
    flywheel.decreaseRPM(50)

def main():
    # led1 = LEDStrip(60)
    # led2 = LEDStrip(60)
    # led3 = LEDStrip(60)
    # led4 = LEDStrip(60)
    # led5 = LEDStrip(60)
    fullStrip1 = LEDStrip(60 * 3)
    fullStrip2 = LEDStrip(60 * 3)

    cs = CommandScheduler()
    cs.addCommand(AuroraCenterInCommand(fullStrip1))
    cs.addCommand(AuroraCenterOutCommand(fullStrip2))
    # cs.addCommand(RainbowCommand(led1, 0))
    # cs.addCommand(PulseColorCommand(led2, YETI_BLUE))
    # cs.addCommand(WaveCommand(led3, YETI_BLUE, Color(136, 11, 219))) # 136, 11, 219 == purple, 0, 255, 195 == blue-green
    # cs.addCommand(BouncyBallCommand(led4, YETI_BLUE, Color(136, 11, 219), 10))
    # cs.addCommand(FlywheelCommand(led5, flywheel))

    root = Root([fullStrip1, fullStrip2], cs, flywheel)
    
    root.bind("<Up>", handleUpKey)
    root.bind("<Down>", handleDownKey)

    while(True):
        root.updateLEDS() 
        root.drawLEDS()
        root.update()

if __name__ == "__main__":
    main()
