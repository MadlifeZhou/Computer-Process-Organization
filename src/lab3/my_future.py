import threading
import logging
import os
from Queue import Queue
RUNNING = 'RUNNING'
PENDING = 'PENDING'
CANCELLED = 'CAMCELLED'
CANCELLED_AND_NOTIFIED = 'CANCELLED_AND_NOTIFIED'
FINISHED = 'FINISHED'

_FUTURE_STATES = [
    PENDING,
    RUNNING,
    CANCELLED,
    CANCELLED_AND_NOTIFIED,
    FINISHED
]

"""
_STATE_TO_DESCRIPTION_MAP = {
    PENDING: "pending",
    RUNNING: "running",
    CANCELLED: "cancelled",
    CANCELLED_AND_NOTIFIED: "cancelled",
    FINISHED: "finished"
}
"""


class Future(object):

    def __init__(self):
        self._condition = threading.Condition()
        self._state = PENDING
        self._result = None
        self._exception = None
        self._waiters = []
        self._done_callbacks = []

    def _invoke_callbacks(self):
        for callback in self._done_callbacks:
            try:
                callback(self)
            except Exception:
                print(F'exception calling callback for {self}')

    def cancel(self):
        with self._condition:
            if self._state in [RUNNING, FINISHED]:
                return False
            if self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]:
                return True
            self._state = CANCELLED
            self._condition.notify_all()
        self._invoke_callbacks()
        return True

    def cancelled(self):
        with self._condition:
            return self._state in [CANCELLED, CANCELLED_AND_NOTIFIED]

    def running(self): #in_progress()
        with self._condition:
            return self._state == RUNNING

    def done(self): #is_done()
        with self._condition:
            return self._state in [CANCELLED, CANCELLED_AND_NOTIFIED, FINISHED]

class ThreadPoolExecutor(_base.Executor):
    def __init__(self, max_workers=None):
        if max_workers is None:
            max_workers = (os.cpu_count() or 1) * 5
        
        if max_workers <= 0:
            raise ValueError('max_worker must be greater than 0')

        self._max_workers = max_workers
        self._work_queue = qu