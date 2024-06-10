import threading
import time


class Sleeper(threading.Thread):
    def __init__(self, sleep=5.0):
        threading.Thread.__init__(self, name='Sleeper')
        self.stop_event = threading.Event()
        self.sleep = sleep

    def run(self):
        print('Thread {thread} started'.format(thread=threading.current_thread()))
        while self.sleep > 0 and not self.stop_event.is_set():
            time.sleep(1.0)
            self.sleep -= 1
        print('Thread {thread} ended'.format(thread=threading.current_thread()))

    def stop(self):
        self.stop_event.set()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args, **kwargs):
        self.stop()
        print('Force set Thread Sleeper stop_event')


with Sleeper(sleep=2.0) as sleeper:
    time.sleep(5)

print('Main Thread ends')
