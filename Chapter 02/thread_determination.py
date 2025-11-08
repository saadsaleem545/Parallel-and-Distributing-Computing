import logging
import threading
import time
import random
from queue import Queue

# Configure logging
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared buffer with limited capacity
buffer = Queue(maxsize=5)

# Event to signal threads to stop
stop_signal = threading.Event()


def producer_thread():
    """Producer keeps adding items until stop_signal is set."""
    while not stop_signal.is_set():
        if not buffer.full():
            item = random.randint(1, 1000)
            buffer.put(item)
            logging.info(f'Produced: {item} | Buffer size: {buffer.qsize()}')
            time.sleep(random.uniform(0.5, 2))
        else:
            logging.info('Buffer full, producer is waiting...')
            time.sleep(1)


def consumer_thread():
    """Consumer keeps removing items until stop_signal is set."""
    while not stop_signal.is_set():
        if not buffer.empty():
            item = buffer.get()
            logging.info(f'Consumed: {item} | Buffer size: {buffer.qsize()}')
            time.sleep(random.uniform(0.5, 2))
        else:
            logging.info('Buffer empty, consumer is waiting...')
            time.sleep(1)


def main():
    # Create producer and consumer threads
    producers = [threading.Thread(target=producer_thread, name=f'Producer-{i+1}') for i in range(2)]
    consumers = [threading.Thread(target=consumer_thread, name=f'Consumer-{i+1}') for i in range(3)]

    # Start all threads
    for thread in producers + consumers:
        thread.start()

    # Let threads run for 10 seconds
    time.sleep(10)
    stop_signal.set()  # Signal threads to stop

    # Wait for all threads to finish
    for thread in producers + consumers:
        thread.join()

    logging.info(f"All threads stopped. Final buffer size: {buffer.qsize()}")


if __name__ == "__main__":
    main()
