import unittest
from my_futures import ThreadPoolExecutor, CancelledError
import time

class TestMyFuture(unittest.TestCase):
    
    def test_done(self):
        exe = ThreadPoolExecutor(max_workers=2)
        f = exe.submit(lambda x:x+1, 1)
        time.sleep(1)
        self.assertEqual(f.done(), True)

    def test_running(self):
        exe = ThreadPoolExecutor(max_workers=2)
        f = exe.submit(lambda: time.sleep(10))
        time.sleep(1)
        self.assertEqual(f.running(), True)

    def test_cancel(self):
        exe = ThreadPoolExecutor(max_workers=1)
        f_1 = exe.submit(lambda: time.sleep(10))
        f_2 = exe.submit(lambda x:x-1, 4)
        f_2.cancel()
        self.assertEqual(f_2.cancelled(), True)

    def test_result(self):
        exe = ThreadPoolExecutor(max_workers=2)
        f_1 = exe.submit(lambda x:x**2, 2)
        f_2 = exe.submit(lambda x:x+5, 3)
        self.assertEqual(f_1.result(), 4)
        self.assertEqual(f_2.result(), 8)

    def test_result_sequence(self):
        """
        From this test, job 2 is queue later than job 1, but it get executed
        before job 1. Because priority has been specified as we want to get job 2
        result first.
        """
        exe = ThreadPoolExecutor(max_workers=1)
        jobs = {lambda: time.sleep(3): {'priority': 2, 'args': []},
                lambda: time.sleep(2): {'priority': 1, 'args': []}}
        fs = exe.submit_with_priority(jobs)
        time.sleep(1)
        self.assertEqual(fs[0].running(), False)
        self.assertEqual(fs[1].running(), True)

    def test_exceptions(self):
        #Number of thread should be greater than 0.
        with self.assertRaises(ValueError):
            ThreadPoolExecutor(max_workers=-1)
        #Timeout error: The maximum waiting time is 1, but future needs 20 time to be done.
        with self.assertRaises(TimeoutError):
            exe = ThreadPoolExecutor(max_workers=1)
            f_1 = exe.submit(lambda: time.sleep(10))
            f_1.result(timeout=1)
        #Cancall error: The job was cancelled, if .result() is called, raised cancelledError.
        with self.assertRaises(CancelledError):
            exe = ThreadPoolExecutor(max_workers=1)
            f_1 = exe.submit(lambda: time.sleep(10))
            f_2 = exe.submit(lambda x:x**2, 2)
            f_2.cancel()
            f_2.result()

if __name__ == '__main__':
    unittest.main()