'''
Python script to enable power from GPIO board to light ring
'''

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError as e:
    print(e)

def enable():
    # Disable warnings 
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)
    
    # Power channel 7 -> 7th header on board
    GPIO.setup(7, GPIO.OUT)

    # Setting output to 'HIGH' turns on
    GPIO.output(7, GPIO.HIGH)
