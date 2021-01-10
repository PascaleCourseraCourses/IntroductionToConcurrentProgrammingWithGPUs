# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and
#   Python.org _thread library documentation at
#   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread
import logging
import _thread
import sys
import time

import pydash as _

from core import thread_function, Core


class StartNewThreadExample:

    def __init__(self):
        self.num_threads = 1
        self.args_conf_list = [['-n', 'num_threads', 1, 'number of concurrent threads to execute']]
        self.core = Core(self.args_conf_list)
        _format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=_format, level=logging.INFO,
                            datefmt="%H:%M:%S")

    def run(self):
        sleeping_time = 0
        for index in range(self.num_threads):
            logging.info("StartNewThreadExample run    : create and start thread %d.", index)
            _thread.start_new_thread(thread_function, (index, ))
            sleeping_time += 1
        # sleep for what should be long enough for threads to complete
        time.sleep(sleeping_time)
        logging.info("StartNewThreadExample completed running threads.")

    def parse_args(self, args):
        namespace = self.core.parse_args(args=args)
        if namespace:
            self.num_threads = int(_.get(namespace, 'num_threads', 1))


if __name__ == "__main__":
    start_new_thread_example = StartNewThreadExample()
    start_new_thread_example.parse_args(args=sys.argv[1:])
    start_new_thread_example.run()
