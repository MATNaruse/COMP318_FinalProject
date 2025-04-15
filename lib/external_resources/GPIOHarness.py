# Handles lighting up LEDs
from time import sleep
from gpiozero import LED

"""WILL NEED TO UPDATE THIS CODE ON RPI LOCALLY"""

# Storing 'pin address index' as value to call from the LEDBoard tuple
LEDDict = {"up": 9, "down": 10, "left": 11, "right": 23, "yes": 24, "no": 25, "go": 24, "stop": 25}


def blink_led(v_input):
    # Sets LED to blink based on passed 'verbal input'
    print(f"Blinking {v_input} - {LEDDict.get(v_input)}")
    led = LED(LEDDict.get(v_input))
    led.on()
    sleep(1)
    led.off()

if __name__ == '__main__':
    blink_led("up")
    blink_led("down")
    blink_led("left")
    blink_led("right")
    blink_led("yes")
    blink_led("no")
