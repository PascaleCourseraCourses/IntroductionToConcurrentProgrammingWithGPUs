# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/
import logging
import time
import argparse
import pydash as _


def thread_function(index):
    logging.info("Thread %d: starting", index)
    time.sleep(1)
    logging.info("Thread %d: finishing", index)


def critical_section_acquire_release(name, sync_object):
    sync_object.acquire()
    thread_function(name)
    sync_object.release()


class Core:

    def __init__(self, args_list=None):
        self.parser = argparse.ArgumentParser(description='Process command-line arguments')
        _.for_each(args_list, self.add_arg_parser_argument)

    def parse_args(self, args) -> argparse.Namespace:
        return self.parser.parse_args(args)

    def add_arg_parser_argument(self, arg):
        self.parser.add_argument(arg[0], dest=arg[1], default=arg[2], help=arg[3])
