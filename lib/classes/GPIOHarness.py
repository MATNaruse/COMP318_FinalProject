# Handles lighting up LEDs
from time import sleep

# from gpiozero import LEDBoard

# Storing 'pin address index' as value to call from the LEDBoard tuple
LEDDict = {"up": 0, "down": 1, "left": 2, "right": 3, "yes": 4, "no": 5}
# leds = LEDBoard(1, 2, 3, 4)


def blink_led(v_input):
    # Sets LED to blink based on passed 'verbal input'
    print(f"Blinking {v_input} - {LEDDict.get(v_input)}")
    # leds.on(LEDDict.get(v_input))
    # sleep(2)
    # leds.off()
    # leds.blink()

if __name__ == '__main__':
    blink_led("up")
