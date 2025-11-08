import multiprocessing
import time
import random


def do_something(size):
    result = []
    for _ in range(size):
        num = random.randint(1, 100)
        result.append(num * num)
    return result


if __name__ == "__main__":
    start_time = time.time()

    size = 1_000_000   
    procs = 5          

    print(f"Running {procs} parallel processes...")

    with multiprocessing.Pool(processes=procs) as pool:

        results = pool.map(do_something, [size] * procs)

    end_time = time.time()

    print("All processes complete.")
    print(f"Multiprocessing time: {end_time - start_time:.2f} seconds")

    print("Example output from one process:", results[0][:10])
