import time 
while 1:
    print(str(time.asctime(time.localtime(time.time()))), end='\r')