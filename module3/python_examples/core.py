# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/
import logging
import random
import time
import argparse


def thread_function(index):
    logging.info("Thread %d: starting", index)
    time.sleep(1)
    logging.info("Thread %d: finishing", index)


def critical_section_acquire_release(name, sync_object):
    # Add random amount of time for sleep so that execution may be random
    time.sleep(random.randint(0, 10))
    sync_object.acquire()
    logging.info("critical_section_acquire_release thread: %d acquired synchronization object.", name)
    thread_function(name)
    sync_object.release()
    logging.info("critical_section_acquire_release thread: %d released synchronization object.", name)


class Core:

    def __init__(self, args_list=None):
        self.parser = argparse.ArgumentParser(description='Process command-line arguments')
        for arg in args_list:
            self.add_arg_parser_argument(arg)

    def parse_args(self, args) -> argparse.Namespace:
        return self.parser.parse_args(args)

    def add_arg_parser_argument(self, arg):
        self.parser.add_argument(arg[0], dest=arg[1], default=arg[2], help=arg[3])
