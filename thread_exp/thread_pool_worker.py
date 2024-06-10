# SuperFastPython.com
# example of calling map() and handling results
import contextvars
import random
from time import sleep
from concurrent.futures import ThreadPoolExecutor

cvar = contextvars.ContextVar("cvar", default="variable")

# task function to be executed in the thread pool
def task(value):
    # sleep for a moment
    xyz = random.choice([1, 2, 3, 10, 9, 8, 4, 5, 6, 7])
    print(value, xyz)
    cvar.set(value)
    sleep(xyz)
    print(f'Task: {value} done. {cvar.get()}')
    # return a message
    return ""


# protect the entry point
if __name__ == '__main__':
    # start the thread pool
    with ThreadPoolExecutor(10) as exe:
        # execute tasks concurrently and process results in order
        for result in exe.map(task, range(10)):
            # report the result
            pass
