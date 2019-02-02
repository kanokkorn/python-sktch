import multiprocessing as mp

import time

def job(a):
    for i in range(10000000):
        a += i

if(__name__=='__main__'):
    pool = mp.Pool(processes=30)
    pool.map(job,range(100))