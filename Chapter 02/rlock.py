import threading
import time
import random
import logging

# Configure logging
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value
            return self.total_items

    def add(self):
        return self.execute(1)

    def remove(self):
        return self.execute(-1)


def adder(box, items):
    logging.info(f'Starting to ADD {items} items')
    while items > 0:
        total = box.add()
        logging.info(f'Added 1 item. Total items now: {total}')
        items -= 1
        time.sleep(1)
    logging.info('Adder finished')


def remover(box, items):
    logging.info(f'Starting to REMOVE {items} items')
    while items > 0:
        total = box.remove()
        logging.info(f'Removed 1 item. Total items now: {total}')
        items -= 1
        time.sleep(1)
    logging.info('Remover finished')


def main():
    box = Box()

    # Randomize number of add/remove operations
    items_to_add = random.randint(10, 20)
    items_to_remove = random.randint(1, 10)

    t1 = threading.Thread(target=adder, name="AdderThread", args=(box, items_to_add))
    t2 = threading.Thread(target=remover, name="RemoverThread", args=(box, items_to_remove))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    logging.info(f'Final total items in box: {box.total_items}')


if __name__ == "__main__":
    main()
