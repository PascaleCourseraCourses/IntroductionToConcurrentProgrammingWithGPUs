# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and
#   Python.org _thread library documentation at
#   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread
import logging
import _thread
import sys
import pydash as _
from threading import BoundedSemaphore

from module3.python_examples.core import Core, critical_section_acquire_release


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
        for index in range(self.num_threads):
            logging.info("ThreadingSemaphoreExample run    : create and start thread %d.", index)
            thread = _thread.start_new_thread(function=critical_section_acquire_release,
                                              args=(index, self.semaphore))
            threads.append(thread)
            thread.start()

        for index, thread in enumerate(threads):
            logging.info("ThreadingSemaphoreExample run    : before joining thread %d.", index)
            thread.join()
            logging.info("ThreadingSemaphoreExample run    : thread %d done", index)


if __name__ == "__main__":
    threadingSemaphoreExample = ThreadingSemaphoreExample()
    threadingSemaphoreExample.parse_args(sys.argv)
    threadingSemaphoreExample.run()
