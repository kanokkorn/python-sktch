import random 
import time 

def compara(x, y):
    if x > y:
        print("X is "+str(x)+" Y is "+str(y))
        return print("Increase")
    if x < y:
        print("X is "+str(x)+" Y is "+str(y))
        return print("Decrease")
    if x == y:
        print("X is "+str(x)+" Y is "+str(y))
        return print("Equal") 


if __name__ == "__main__":
    b = [0, 0]
    try:
        for x in range(100):
            b[0] = random.randint(0, 100)
            compara(b[0],b[1])
            b[1] = b[0]
            time.sleep(0.5) 

    except KeyboardInterrupt as err:
        raise Exception
        exit()
