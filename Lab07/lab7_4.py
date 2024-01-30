import RPi.GPIO as GPIO
import time
import drivers

display = drivers.Lcd()
display.lcd_clear()

SW1  = 27  
SW2  = 17

lcd_position = -1
name = ["Tuchpol","Piyathida","Nutthanicha"]
code = ["116510400344-7","116510462012-5","116510462025-7"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

try:
    while True:
	
        if GPIO.event_detected(SW1):
            lcd_position += 1
            if lcd_position >= 3:
                lcd_position = -1
            display.lcd_clear()
            display.lcd_display_string(name[lcd_position], 1)
            display.lcd_display_string(code[lcd_position], 2)
            
        elif GPIO.event_detected(SW2):
            GPIO.remove_event_detect(SW1)
            GPIO.remove_event_detect(SW2)
            GPIO.cleanup()
            display.lcd_clear()
            print("\nBye...")
            break
        time.sleep(0.5)

except KeyboardInterrupt:

    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()

    display.lcd_clear()
    print("\nBye...")
