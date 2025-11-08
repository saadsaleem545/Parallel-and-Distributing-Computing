import logging
import threading
import time
from queue import Queue

# Configure logging
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared queue
buffer = Queue(maxsize=10)

class Producer(threading.Thread):
    def __init__(self, name, buffer):
        super().__init__(name=name)
        self.buffer = buffer

    def run(self):
        for i in range(20):
            item = f"item-{i}"
            time.sleep(0.5)  # simulate work
            self.buffer.put(item)
            logging.info(f'Produced {item} (queue size={self.buffer.qsize()})')


class Consumer(threading.Thread):
    def __init__(self, name, buffer):
        super().__init__(name=name)
        self.buffer = buffer

    def run(self):
        for i in range(20):
            time.sleep(2)  # simulate slower consumption
            item = self.buffer.get()
            logging.info(f'Consumed {item} (queue size={self.buffer.qsize()})')
            self.buffer.task_done()


def main():
    producer = Producer(name='Producer', buffer=buffer)
    consumer = Consumer(name='Consumer', buffer=buffer)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    logging.info('All work completed.')


if __name__ == "__main__":
    main()
