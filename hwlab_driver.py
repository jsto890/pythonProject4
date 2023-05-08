import machine, microbit

OUT_address = 0x50000504
OUT_SET_address = 0x50000508
OUT_CLEAR_address = 0x5000050C

microbit.display.off()

rows = [13, 14, 15]
columns = [4, 5, 6, 7, 8, 9, 10, 11, 12]


def clear_display():
    """
    Turn off all pixels.
    """
    machine.mem16[OUT_CLEAR_address] = 0b1110001111111110


def illuminate_display():
    """
    Turn on all pixels.
    """
    machine.mem16[OUT_SET_address] = 0b1110000000000000
    machine.mem16[OUT_CLEAR_address] = 0b0001111111111110


def display_pixel(row, column):
    """
    Turn on one specific pixel.
    """
    clear_display()

    # Hardcoded pin assignments for each LED
    pixel_to_pins = [
        [(13, 4), (14, 7), (13, 5), (14, 8), (13, 6)],
        [(15, 7), (15, 9), (15, 10), (15, 11), (15, 12)],
        [(14, 4), (13, 9), (14, 5), (15, 9), (13, 8)],
        [(13, 7), (13, 6), (13, 5), (13, 4), (15, 3)],
        [(15, 6), (14, 10), (15, 8), (14, 11), (15, 9)]]

    power_pin, ground_pin = pixel_to_pins[row][column]

    machine.mem16[OUT_SET_address] = 1 << power_pin
    machine.mem16[OUT_CLEAR_address] = 1 << ground_pin


def main():
    """
    Standalone test of device driver.
    """

    display_pixel(2, 2)
    microbit.sleep(1000)
    display_pixel(1, 1)
    microbit.sleep(1000)

    clear_display()
    microbit.sleep(1000)
    display_pixel(2, 2)
    microbit.sleep(1000)
    illuminate_display()
    microbit.sleep(1000)
    clear_display()


if __name__ == "__main__":
    main()

