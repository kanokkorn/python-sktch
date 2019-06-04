#!/usr/bin/python3

import random
import time


def bet():
    value = random.random()
    if value < 0.4462:
        return 0
    if value < 0.9047 and value >= 0.4462 :
        return 1
    else:
        return 2


if __name__ == "__main__":
    cout_a = cout_b = cout_c = 0
    for i in range(100):
        if bet() == 0:
            cout_a += 1
        elif bet() == 1:
            cout_b += 1
        elif bet() == 2:
            cout_c += 1
        print(bet())
        time.sleep(0.02)
    print(" === Result === \n Player: %d times\n Banker: %d times\n Draw: %d times" % (cout_a, cout_b, cout_c))

