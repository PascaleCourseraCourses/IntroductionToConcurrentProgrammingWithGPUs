# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and
#   Python.org _thread library documentation at
#   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread
import logging

import sys
import time

import pydash as _
from threading import BoundedSemaphore, Thread, active_count

from core import Core, critical_section_acquire_release


class ThreadingSemaphoreExample:

    def __init__(self):
        self.num_threads = 1
        self.semaphore_size = 1
        self.semaphore = None
        self.args_conf_list = [
            ['-n', 'num_threads', 1, 'number of concurrent threads to execute'],
            ['-s', 'semaphore_size', 1, 'maximum number of threads that can hold a semaphore']
        ]
        self.core = Core(self.args_conf_list)
        _format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=_format, level=logging.INFO,
                            datefmt="%H:%M:%S")

    def parse_args(self, argv):
        namespace = self.core.parse_args(argv)
        if namespace:
            self.num_threads = int(_.get(namespace, 'num_threads', 1))
            self.semaphore_size = int(_.get(namespace, 'semaphore_size', 1))
        self.semaphore = BoundedSemaphore(value=self.semaphore_size)

    def run(self):
        threads = list()
        # Need an initial count of threads running in process for future calculation
        initial_num_threads = active_count()
        for index in range(self.num_threads):
            logging.info("ThreadingSemaphoreExample run    : create and start thread %d.", index)
            thread = Thread(group=None, target=critical_section_acquire_release, args=(index, self.semaphore))
            threads.append(thread)
            thread.start()

        while active_count() > initial_num_threads:
            logging.info("Waiting for no active threads. Number of active threads: %d", active_count() -
                         initial_num_threads)
            time.sleep(1)

        logging.info("There are no longer any active threads and the program will exit.")


if __name__ == "__main__":
    threadingSemaphoreExample = ThreadingSemaphoreExample()
    threadingSemaphoreExample.parse_args(sys.argv[1:])
    threadingSemaphoreExample.run()
