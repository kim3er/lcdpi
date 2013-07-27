import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)
GPIO.add_event_detect(4, GPIO.BOTH)
def my_callback(arg):
    GPIO.output(17, GPIO.input(4))
GPIO.add_event_callback(4, my_callback)

while True:
    print "Waiting for input."                     # Insert Random Loop Junk
    sleep(60);                           # Sleeps for a minute to save CPU cycles.  Any interrupt will break this.

GPIO.cleanup()