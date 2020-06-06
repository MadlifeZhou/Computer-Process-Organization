import threading
from queue import Queue, PriorityQueue
import time

def _worker(work_queue, priority=False):
    """
    This function will be executed by every thread.
    In this infinite while loop, every thread get a work_item from the work_queue,
    if get a None type value, it will be blocked itself. Once there is a new work item
    putted into the work_queue, one of the threads will be waken and execute the corresponding function.
    """
    while True:
        work_item = work_queue.get(block=True)
        #print(F'{id(work_item)} has been removed from the queue.\n')
        if work_item is not None:
            work_item.run()
            del work_item
            work_queue.task_done()
            continue



class ThreadPoolExecutor(object):
    """
    Global worker pool.
    """
    def __init__(self, max_workers=None, priority=False):
        if max_workers is None:
            max_workers = 2
        elif max_workers <= 0:
            raise ValueError('max_workers must be greater than 0')
        
        self._max_workers = max_workers #The maximum number of threads allowed to be created.
        self._work_queue = PriorityQueue() #A queue where stores jobs to be done.
        self._threads = set() #Number of the running threads.
        #self._priority = priority



    def submit(self, fn, *args, **kwargs):
        f = Future()
        w = _WorkItem(None, f, fn, args, kwargs)
        self._work_queue.put(w)
        #print(F'{id(w)} has been putted into the queue.\n')
        self._start_working()

        return f #Return future.



    def submit_with_priority(self, fn_dict):
        """
        This method recieves a dictionary of functions. Priority can be specified,
        and the smaller value indicates higher priority.
        i.e. If I have 2 job(job 1, job 2), and job 2 is queued later than job 1, but
        I want to get result of job 2 first, so I got to set a higher priority than job 1.
        As a result, job 2 will be executed before job 1.
        """
        fs = []
        for fn in fn_dict.keys():
            f = Future()
            fs.append(f)
            w = _WorkItem(fn_dict[fn]['priority'], f, fn, fn_dict[fn]['args'])
            self._work_queue.put(w)
            #print(F'{id(w)} has been putted into the queue.\n')
        for thread_num in range(self._max_workers):
            self._start_working()
        return fs



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
    def __init__(self, priority, future, fn, args, kwargs=None):
        self.future = future
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.priority = priority

    def run(self):
        """
        This method is actually running requested function.
        """
        self.future.set_running()
        if self.kwargs is None: result = self.fn(*self.args)
        else: result = self.fn(*self.args, *self.kwargs)
        self.future.set_result(result)

    def __lt__(self, other):
        return self.priority <= other.priority




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
    def __init__(self):
        self.msg = 'Future has been cancelled.'
        print(self.msg)