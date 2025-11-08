import multiprocessing
from multiprocessing import Barrier, Lock, Process, Manager
from time import time, sleep
from datetime import datetime

def test_with_barrier(synchronizer, serializer, completed_list):
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait for other processes
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))
    completed_list.append((name, datetime.fromtimestamp(now)))

def test_without_barrier(completed_list):
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))
    completed_list.append((name, datetime.fromtimestamp(now)))

if __name__ == '__main__':
    manager = Manager()
    completed_list = manager.list()  # Shared list to track process completion

    synchronizer = Barrier(2)
    serializer = Lock()

    processes = [
        Process(name='p1 - test_with_barrier',
                target=test_with_barrier, args=(synchronizer, serializer, completed_list)),
        Process(name='p2 - test_with_barrier',
                target=test_with_barrier, args=(synchronizer, serializer, completed_list)),
        Process(name='p3 - test_without_barrier',
                target=test_without_barrier, args=(completed_list,)),
        Process(name='p4 - test_without_barrier',
                target=test_without_barrier, args=(completed_list,))
    ]

    # Start all processes
    for p in processes:
        p.start()

    # Wait for all to finish
    for p in processes:
        p.join()

    #  Summary of completion order
    print("\nAll processes finished! Completion order:")
    for idx, (name, timestamp) in enumerate(completed_list, start=1):
        print(f"{idx}. {name} at {timestamp}")
