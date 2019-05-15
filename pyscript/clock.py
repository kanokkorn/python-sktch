import time


def display_time():
    return print(str(time.asctime(time.localtime(time.time()))), end="\r")


if __name__ == "__main__":
    try:
        while True:
            display_time()
    except KeyboardInterrupt as err:
        print("Keyboard Interrupt... Stopped")
