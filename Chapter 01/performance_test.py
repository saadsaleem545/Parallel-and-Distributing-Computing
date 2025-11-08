import os
import time
import threading
import multiprocessing
import random

# Configuration
NUM_WORKERS = 10
SIZE = 1_000_000


def do_something(count, out_list):
    """Simple function — random numbers generate karta hai"""
    for _ in range(count):
        out_list.append(random.random())


if __name__ == "__main__":

    # ---------------- SERIAL EXECUTION ----------------
    start_time = time.time()
    out_list = []
    for _ in range(NUM_WORKERS):
        do_something(SIZE, out_list)
    end_time = time.time()
    print("\n🧮 Serial time =", round(end_time - start_time, 2), "seconds")

    # ---------------- MULTITHREADING ----------------
    start_time = time.time()
    out_list = []
    jobs = []

    for i in range(NUM_WORKERS):
        thread = threading.Thread(target=do_something, args=(SIZE, out_list))
        jobs.append(thread)

    # Start all threads
    for j in jobs:
        j.start()

    # Wait for all threads
    for j in jobs:
        j.join()

    end_time = time.time()
    print(" Threading time =", round(end_time - start_time, 2), "seconds")

    # ---------------- MULTIPROCESSING ----------------
    start_time = time.time()
    manager = multiprocessing.Manager()
    out_list = manager.list()  # Shared list for processes
    jobs = []

    for i in range(NUM_WORKERS):
        process = multiprocessing.Process(target=do_something, args=(SIZE, out_list))
        jobs.append(process)

    # Start all processes
    for j in jobs:
        j.start()

    # Wait for all to finish
    for j in jobs:
        j.join()

    end_time = time.time()
    print(" Multiprocessing time =", round(end_time - start_time, 2), "seconds")

    print("\n List processing complete.")
