"""
Hardware Lab device driver exercise.
Use this version with the simulator only.

Please note that this simulator requires use of asynchronous
programming - microbit.sleep(), microbit.display.show(), and
microbit.display.scroll() must be called with the "await"
keyword, any functions calling these must be declared with the
"async" keyword, and any time you call your own async functions
you also need to use await.

For this assignment, please do not use microbit.sleep() except
within the main() function.

Description: Control individual pixels on the micro:bit display using low-level functions.
"""

import machine, microbit

OUT_address = 0x50000504
OUT_SET_address = 0x50000508
OUT_CLEAR_address = 0x5000050C

microbit.display.off()


def clear_display():
    """
    Turn off all pixels.
    """
    for row in range(5):
        for col in range(5):
            microbit.display.set_pixel(row, col, 0)


def illuminate_display():
    """
    Turn on all pixels.
    """
    for row in range(5):
        for col in range(5):
            microbit.display.set_pixel(row, col, 9)


def display_pixel(row, column):
    """
    Turn on one specific pixel.
    """
    clear_display()
    microbit.display.set_pixel(row, column, 9)


async def main():
    """
    Standalone test of device driver.
    """

    display_pixel(2, 2)
    await microbit.sleep(1000)
    display_pixel(1, 1)

    clear_display()
    await microbit.sleep(1000)
    display_pixel(2, 2)
    await microbit.sleep(1000)
    illuminate_display()
    await microbit.sleep(1000)
    clear_display()

if __name__ == "__main__":
    microbit.run(main)