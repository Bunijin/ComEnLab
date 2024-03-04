import RPi.GPIO as GPIO
import time

pin_seg = [17,27,22]

SW = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_seg, GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
try:
    while True:
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    if GPIO.wait_for_edge(SW, GPIO.FALLING):
                        GPIO.output(pin_seg[0], i)
                        GPIO.output(pin_seg[1], j)
                        GPIO.output(pin_seg[2], k)
                    time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
 
print("\nBye…")
