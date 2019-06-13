import random
import time


def compara(x, y):
    if x > y:
        return print("X is %.3d | Y is %.3d | Increase"%(x, y))

    if x < y:
        return print("X is %.3d | Y is %.3d | Decrease"%(x, y))

    if x == y:
        return print("X is %.3d | Y is %.3d | Equal"%(x, y))


if __name__ == "__main__":
    b = [0, 0]
    try:
        for x in range(100):
            b[0] = random.randint(0, 100)
            compara(b[0], b[1])
            b[1] = b[0]
            time.sleep(0.5)

    except KeyboardInterrupt as err:
        raise Exception
        exit()
