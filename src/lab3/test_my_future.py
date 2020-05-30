import unittest
from my_futures import ThreadPoolExecutor
import time

class TestMyFuture(unittest.TestCase):
    
    def test_done(self):
        exe = ThreadPoolExecutor(max_workers=2)
        f = exe.submit(lambda x:x+1, 1)
        self.assertEqual(f.done(), True)

    def test_running(self):
        def worker():
            time.sleep(10)
        exe = ThreadPoolExecutor(max_workers=2)
        f = exe.submit(worker)
        self.assertEqual(f.running(), True)

    def test_cancel(self):
        def worker():
            time.sleep(10)
        exe = ThreadPoolExecutor(max_workers=1)
        f_1 = exe.submit(worker)
        f_2 = exe.submit(lambda x:x-1, 4)
        f_2.cancel()
        self.assertEqual(f_2.cancelled(), True)

    def test_result(self):
        exe = ThreadPoolExecutor(max_workers=2)
        f_1 = exe.submit(lambda x:x**2, 2)
        f_2 = exe.submit(lambda x:x+5, 3)
        self.assertEqual(f_1.result(), 4)
        self.assertEqual(f_2.result(), 8)

if __name__ == '__main__':
    unittest.main()