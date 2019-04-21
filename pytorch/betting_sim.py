import random
import time


def bet():
    value = random.random()
    if value < 0.4462:
        return 0
    if value < 0.9047:
        return 1
    else:
        return 2


if __name__ == "__main__":
    cout_a = cout_b = 0
    for i in range(100):
        if bet() == 0:
            cout_a += 1
        if bet() == 1:
            cout_b += 1
    print(" === Result === \n Player: %d times\n Banker: %d times" % (cout_a, cout_b))

