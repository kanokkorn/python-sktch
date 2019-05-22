import multiprocessing as mp

import time


def job(a):
    for i in range(10000000):
        a += i


if __name__ == "__main__":
    sec_start = time.time()
    pool = mp.Pool(processes=30)
    pool.map(job, range(100))
    sec_end = time.time()
    print("Time use: %f s" % (sec_end - sec_start))
