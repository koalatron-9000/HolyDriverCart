#imports
import RPi.GPIO as GPIO
import sys


#pin initialization
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)
def relay_switch(x):
    if isinstance(x, int):
        if x == 1:
            GPIO.output(11,1)
            print("On!")
        if x == 0:
            GPIO.output(11,0)
            print("Off!")
    else:
        if str(x[1]) =="1":
            GPIO.output(11,1)
            print("On!")
        if str(x[1]) == "0":
            GPIO.output(11,0)
   
if __name__ == "__main__":
    relay_switch(sys.argv)
