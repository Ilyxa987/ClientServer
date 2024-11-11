from multiprocessing import Process
import os
import random


def f(start):
    for i in range(start, 1000, 4):
        with open(f'Files\\file{i}.txt', 'wb') as f:
          f.write(os.urandom(random.randint(50000000, 100000000)))

if __name__ == '__main__':
    for i in range(4):
        p = Process(target=f, args=(i,))
        p.start()
