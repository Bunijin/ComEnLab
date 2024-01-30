import RPi.GPIO as GPIO
import time

SW1  = 27  
SW2  = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
	
        if GPIO.wait_for_edge(SW1, GPIO.FALLING):
            print("SW1 Pressed")

        elif GPIO.wait_for_edge(SW2, GPIO.FALLING): 
            print("SW2 Pressed") 

        time.sleep(0.3)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye..")
