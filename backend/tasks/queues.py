# encoding: utf-8
"""
Task: Queues
---------
Holds various queues which are used by background tasks, some queues might be very simple, but some might be very complex.
"""
from queue import Queue

QUEUE_DOWNLOADER = Queue()  # task_id goes into this
QUEUE_CONVERTER = Queue()  # task_id goes into this