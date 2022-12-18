# encoding: utf-8
"""
Task: Queues
---------
Holds various queues which are used by background tasks, some queues might be very simple, but some might be very complex.
"""
from queue import Queue

QUEUE_DOWNLOADER = Queue()  # Doesn't matter what value goes into it, placement will trigger the downloader