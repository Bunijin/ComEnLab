import RPi.GPIO as GPIO
import time

SW = 22
LED = 18
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            if count != 0:
                GPIO.output (LED, False)
                count = 0
                print("\nLED => Off")
                time.sleep(0.1)
            else:
                GPIO.output (LED, True)
                count = 1
                print("\nLED => On")
                time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye")
