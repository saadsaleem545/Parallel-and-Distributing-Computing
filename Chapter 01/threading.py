from do_something import *
import time
import threading

if __name__ == "__main__":  
    start_time = time.time()  
    size = 1_000_000          
    threads = 5               
    jobs = []                 

    # Threads create kar rahe hain
    for i in range(threads):
        out_list = []   # Har thread apni ek alag list me data daalega
        # Thread banate waqt target function aur uske arguments dene hote hain
        thread = threading.Thread(target=do_something, args=(size, out_list))
        jobs.append(thread)

    # Ab saare threads start kar do
    for j in jobs:
        j.start()

    # Wait karte hain jab tak saare threads apna kaam complete na kar lein
    for j in jobs:
        j.join()

    # Jab sab complete ho jaye
    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", round(end_time - start_time, 2), "seconds")
