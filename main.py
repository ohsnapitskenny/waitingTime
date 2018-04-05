import RPi.GPIO as GPIO
import RPi_I2C_driver
import MFRC522
import signal
from time import *

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()
    pass

def get_time():
    mylcd.lcd_display_string("Time remaining", 1)
    mylcd.lcd_display_string("30 minutes", 2)
    pass


signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Starting MFRC522 data reader"
print "Press Ctrl-C to stop."

mylcd = RPi_I2C_driver.lcd()

while continue_reading:

    get_time()

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Reservation has", 1)
        mylcd.lcd_display_string("been made!", 2)
        sleep(5)
