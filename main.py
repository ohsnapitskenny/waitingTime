import RPi.GPIO as GPIO
import RPi_I2C_driver
import MFRC522
import signal

continue_reading = True

def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

signal.signal(signal.SIGINT, end_read)
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Starting MFRC522 data reader"
print "Press Ctrl-C to stop."
mylcd = RPi_I2C_driver.lcd()
mylcd.lcd_display_string("Havenlab", 1)
mylcd.lcd_display_string("Time remaining", 2)


while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        mylcd.lcd_clear()
        mylcd.lcd_display_string("Reservation made")