import drivers
from time import sleep

display = drivers.Lcd()
display.lcd_clear()

try:
 while True:
   print("Writing to LCD !!!")
   display.lcd_display_string("Lab7-LCD", 1)
   display.lcd_display_string("Hello World", 2)
   sleep(2)
   
   display.lcd_display_string("I am Engineer", 1)
   display.lcd_display_string("0123456789abcdef", 2)
   sleep(2)
	
   display.lcd_clear()
   sleep(2)

except KeyboardInterrupt:

   display.lcd_clear()
   print("\nBye...")
