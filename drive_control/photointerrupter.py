# This code will detect changes in the photointerrupter status
# and print the results to the terminal window upon detection
# of a change in status

import RPi.GPIO as GPIO
import time
 
def setup():
    # Set GPIO as PIN Numbers 
    GPIO.setmode(GPIO.BCM) 
    # Initalize the GPIO input for the photointerrupter
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(26, GPIO.BOTH, callback=detect, bouncetime=1)
     
def print_status(x):
    # Prints the current status of the photointerrupter (either interrupted and not interrupted)
    if x == 1:
        print('1 - not interrupted')
    else:
        print('0 - interrupted')
    
     
def detect(chn):
    # When a change in status is detected by the photointerrupter, this function will be called
    print_status(GPIO.input(26))
    
 
def loop():
    while True:
        pass
 
def destroy():
    GPIO.cleanup() # Release resource
 
if __name__ == '__main__': # Set the Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When pressed 'Ctrl+C' child program destroy() will be executed.
        destroy()
