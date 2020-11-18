import multiprocessing
from player import *

with multiprocessing.Manager() as manager:
    name=("cirano")
    p1 = multiprocessing.Process(target=play,args=(name,))
    p1.start()
    #p1.join()



