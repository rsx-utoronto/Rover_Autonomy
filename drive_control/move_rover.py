# code to move the rover forward and backwards with only one motor controller
import RPi.GPIO as gpio
import time

def init():
    # initialize the GPIO pins
    # (pin numbers will change depending on how the motor controller was connected to the RPi)
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
    
    
def forward(sec):
    # GPIO output to spin the motors in the direction that moves the rover forward
    # input is the time desired (in secs) for the motors to spin
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(sec)
    gpio.cleanup()
    
def reverse(sec):
    # GPIO output to spin the motors in the direction that moves the rover backwards
    # input is the time desired (in secs) for the motors to spin
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(sec)
    gpio.cleanup()


if __name__ == '__main__': # Set the Program start from here
    init()

    # main program, use the forward or reverse functions to move the rover
    print("forward")
    forward(4)
