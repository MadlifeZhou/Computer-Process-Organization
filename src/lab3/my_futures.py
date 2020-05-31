import threading
from queue import Queue
import time

def _worker(work_queue):
    """
    This function will be executed by every thread.
    In this infinite while loop, every thread get a work_item from the work_queue,
    if get a None type value, it will be blocked itself. Once there is a new work item
    putted into the work_queue, one of the threads will be waken and execute the corresponding function.
    """
    while True:
        work_item = work_queue.get(block=True)
        if work_item is not None:
            work_item.run()
            del work_item
            work_queue.task_done()
            continue

class ThreadPoolExecutor(object):
    """
    Global worker pool.
    """
    def __init__(self, max_workers=None):
        if max_workers is None:
            max_workers = 2
        elif max_workers <= 0:
            raise ValueError('max_workers must be greater than 0')
        
        self._max_workers = max_workers #The maximum number of threads allowed to be created.
        self._work_queue = Queue() #A queue where stores jobs to be done.
        self._threads = set() #Number of the running threads.


    def submit(self, fn, *args, **kwargs):
        f = Future()
        w = _WorkItem(f, fn, args, kwargs)
        self._work_queue.put(w)
        #print(self._work_queue.qsize())
        self._start_working()

        return f #Return future.
    

    def _start_working(self):
        """
        Wake worker thread.
        """
        if len(self._threads) < self._max_workers: #Running threads must smaller than maximum.
            t = threading.Thread(target=_worker, args=(self._work_queue,))
            t.daemon = True #When main thread quits, children threads quit as well.
            t.start()
            self._threads.add(t)

    def shutdown(self):
        self._work_queue.join()

class _WorkItem(object):
    def __init__(self, future, fn, args, kwargs):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        """
        This method is actually running requested function.
        """
        self.future.set_running()
        result = self.fn(*self.args, *self.kwargs)
        self.future.set_result(result)

class Future(object):
    def __init__(self):
        self._result = None
        self._condition = threading.Condition()
        self._state = 'PENDING'

    def done(self):
        with self._condition:
            return self._state == 'FINISHED'

    def running(self):
        with self._condition:
            return self._state == 'RUNNING'

    def cancelled(self):
        with self._condition:
            return self._state == 'CANCELLED'

    def result(self, timeout=None):
        """
        If state of future is 'FINISHED', return result directly.
        Otherwise, wait until other thread's notification, or exceed time limit(timeout).
        """
        with self._condition:
            if self._state == 'CANCELLED':
                raise CancelledError()
            elif self._state == 'FINISHED':
                return self._result
            self._condition.wait(timeout) #Block until future is done.
            if self._state == 'CANCELLED':
                raise CancelledError()
            elif self._state == 'FINISHED':
                return self._result
            else:
                raise TimeoutError #Timeout.
    def set_result(self, result):
        with self._condition:
            self._result = result
            self._state = 'FINISHED'
            self._condition.notify_all()


    def cancel(self):
        if self._state in ['RUNNING', 'FINISHED']:
            return False
        else:
            self.set_cancelled()

    def set_running(self):
        self._state = 'RUNNING'
    def set_finished(self):
        self._state = 'FINISHED'
    def set_cancelled(self):
        self._state = 'CANCELLED'
class CancelledError(Exception):
    pass
