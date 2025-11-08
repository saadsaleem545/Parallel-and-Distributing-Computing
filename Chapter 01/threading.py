from do_something import *
import time
import threading

if __name__ == "__main__":  
    start_time = time.time()  
    size = 1_000_000          
    threads = 5               
    jobs = []                 

    
    for i in range(threads):
        out_list = []  
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", round(end_time - start_time, 2), "seconds")
