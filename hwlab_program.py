"""
Hardware Lab device driver exercise 4.
Use this version with the simulator only.

Please note that the simulator requires use of asynchronous
programming - microbit.sleep(), microbit.dislay.show(), and
microbit.display.scroll() must be called with the "await"
keyword, any functions calling these must be declared with the
"async" keyword, and any time you call your own async functions
you also need to use await.

Description: Moves a pixel around the display on a micro:bit.
"""

import microbit
from hwlab_driver import display_pixel  # Import display_pixel function from hwlab_driver


async def main():
    while True:
        for n in range(25):
            x = int(n / 5)
            y = n % 5
            # Call function in device driver to light pixel in row x, column y
            display_pixel(x, y)
            await microbit.sleep(500)


if __name__ == "__main__":
    microbit.run(main)
