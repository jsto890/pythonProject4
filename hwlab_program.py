import microbit
from hwlab_driver import display_pixel  # Import display_pixel function from hwlab_driver


def main():
    while True:
        for n in range(25):
            x = int(n / 5)
            y = n % 5
            # Call function in device driver to light pixel in row x, column y
            display_pixel(x, y)
            microbit.sleep(500)


if __name__ == "__main__":
    main()