import RPi.GPIO as GPIO
import time

SW = 22
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING):
            count = count + 1
            print(f"Button Pressed {count}")
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye")
