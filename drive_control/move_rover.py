# code to move the rover forward and backwards with only one motor controller
import RPi.GPIO as gpio
import time

def init():
    # initialize the GPIO pins
    # (pin numbers will change depending on how the motor controller was connected to the RPi)
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.OUT)
    gpio.setup(19, gpio.OUT)
    gpio.setup(20, gpio.OUT)
    gpio.setup(26, gpio.OUT)
    
    gpio.setup(8, gpio.OUT)
    gpio.setup(9, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(25, gpio.OUT)
    
    
def forward(sec):
    # GPIO output to spin the motors in the direction that moves the rover forward
    # input is the time desired (in secs) for the motors to spin
    init()
    
    gpio.output(16, gpio.HIGH)
    gpio.output(19, gpio.LOW)
    gpio.output(20, gpio.LOW)
    gpio.output(26, gpio.HIGH)
    
    gpio.output(8, gpio.HIGH)
    gpio.output(9, gpio.LOW)
    gpio.output(11, gpio.HIGH)
    gpio.output(25, gpio.LOW)
    
    time.sleep(sec)
    gpio.cleanup()
    
def reverse(sec):
    # GPIO output to spin the motors in the direction that moves the rover backwards
    # input is the time desired (in secs) for the motors to spin
    init()
    
    gpio.output(16, gpio.LOW)
    gpio.output(19, gpio.HIGH)
    gpio.output(20, gpio.HIGH)
    gpio.output(26, gpio.LOW)
    
    gpio.output(8, gpio.LOW)
    gpio.output(9, gpio.HIGH)
    gpio.output(11, gpio.LOW)
    gpio.output(25, gpio.HIGH)
    time.sleep(sec)
    gpio.cleanup()


if __name__ == '__main__': # Set the Program start from here

    # main program, use the forward or reverse functions to move the rover
    print("forward 1 sec")
    forward(1)
    
    time.sleep(0.5)
    
    print("reverse")
    reverse(1)
