'''
Code for Movement of Rover with all four motors
'''

import RPi.GPIO as gpio
import time

# Back Right Wheel
back_in1 = 20
back_in2 = 16

# Back Left Wheel
back_in3 = 26
back_in4 = 19

# Front Left Wheel
front_in1 = 9
front_in2 = 11

# Front Right Wheel
front_in3 = 25
front_in4 = 8

def init():
    # initialize the GPIO pins
    # (pin numbers will change depending on how the motor controller was connected to the RPi)
    gpio.setmode(gpio.BCM)
    gpio.setup(back_in1, gpio.OUT)
    gpio.setup(back_in2, gpio.OUT)
    gpio.setup(back_in3, gpio.OUT)
    gpio.setup(back_in4, gpio.OUT)

    gpio.setup(front_in1, gpio.OUT)
    gpio.setup(front_in2, gpio.OUT)
    gpio.setup(front_in3, gpio.OUT)
    gpio.setup(front_in4, gpio.OUT)
    
    
def forward(sec):
    # GPIO output to spin the motors in the direction that moves the rover forward
    # input is the time desired (in secs) for the motors to spin
    
    # For Back
    gpio.output(back_in4, True)
    gpio.output(back_in3, False)
    gpio.output(back_in1, False)
    gpio.output(back_in2, True)

    # For Front
    gpio.output(front_in4, False)
    gpio.output(front_in3, True)
    gpio.output(front_in1, True)
    gpio.output(front_in2, False)

    time.sleep(sec)
    gpio.cleanup()
    
def reverse(sec):
    # GPIO output to spin the motors in the direction that moves the rover backwards
    # input is the time desired (in secs) for the motors to spin
    # For Back
    gpio.output(back_in4, False)
    gpio.output(back_in3, True)
    gpio.output(back_in1, True)
    gpio.output(back_in2, False)

    # For Front
    gpio.output(front_in4, True)
    gpio.output(front_in3, False)
    gpio.output(front_in1, False)
    gpio.output(front_in2, True)

    time.sleep(sec)
    gpio.cleanup()

def right(sec):
    # GPIO output to spin the motors in the direction that turns the rover right
    # input is the time desired (in secs) for the motors to spin
    # For Back
    gpio.output(back_in4, True)
    gpio.output(back_in3, False)
    gpio.output(back_in1, True)
    gpio.output(back_in2, False)

    # For Front
    gpio.output(front_in4, True)
    gpio.output(front_in3, False)
    gpio.output(front_in1, True)
    gpio.output(front_in2, False)

    time.sleep(sec)
    gpio.cleanup()

def left(sec):
    # GPIO output to spin the motors in the direction that turns the rover left
    # input is the time desired (in secs) for the motors to spin
    # For Back
    gpio.output(back_in4, False)
    gpio.output(back_in3, True)
    gpio.output(back_in1, False)
    gpio.output(back_in2, True)

    # For Front
    gpio.output(front_in4, False)
    gpio.output(front_in3, True)
    gpio.output(front_in1, False)
    gpio.output(front_in2, True)

    time.sleep(sec)
    gpio.cleanup()

def stop(sec):
    # GPIO output to stop motion of motors
    # Mainly used for reseting values after use
    
    # For Back
    gpio.output(back_in4, False)
    gpio.output(back_in3, False)
    gpio.output(back_in1, False)
    gpio.output(back_in2, False)

    # For Front
    gpio.output(front_in4, False)
    gpio.output(front_in3, False)
    gpio.output(front_in1, False)
    gpio.output(front_in2, False)

    time.sleep(sec)
    gpio.cleanup()
    
if __name__ == '__main__': # Set the Program start from here

    # main program, providing letter input will initiate rover motion.
    
    sec = 2
    print("Begin Program")
    while(True):
        init()
        action = input('\nDirection? (f : Forward | b : Backward | r : Right | l : Left | q : Quit)\n')
        if (action == ('f')):
            forward(sec)
        elif (action == 'b'):
            reverse(sec)
        elif (action == 'r'):
            right(sec)
        elif (action == 'l'):
            left(sec)
        elif (action == 'q'):
            stop(1)
            break

        init()
        stop(1)