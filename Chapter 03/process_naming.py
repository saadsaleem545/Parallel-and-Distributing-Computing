import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name
    print("Starting process name = %s \n" % name)
    start_time = time.time()
    time.sleep(3)
    end_time = time.time()
    print("Exiting process name = %s \n" % name)
    return end_time - start_time  # Process execution time

if __name__ == '__main__':
    process_times = multiprocessing.Manager().list()  # Shared list to store process times

    def wrapper(func, process_times):
        elapsed = func()
        process_times.append((multiprocessing.current_process().name, elapsed))

    # Create processes
    process_with_name = multiprocessing.Process(
        name='myFunc process',
        target=wrapper,
        args=(myFunc, process_times)
    )

    process_with_default_name = multiprocessing.Process(
        target=wrapper,
        args=(myFunc, process_times)
    )

    # Start processes
    process_with_name.start()
    process_with_default_name.start()

    # Wait for processes to finish
    process_with_name.join()
    process_with_default_name.join()

    #  Final summary
    print("\nAll processes finished! Execution times:")
    for name, elapsed in process_times:
        print(f"{name} ran for {elapsed:.2f} seconds")
