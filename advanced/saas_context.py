import threading


class SaasContext(threading.Thread):
    _params: dict = None
    _tkey: str = None
    _method = None

    def __init__(self, tkey: str, method):
        threading.Thread.__init__(self)
        self._tkey = tkey
        self._method = method

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.join()

    def run(self):
        if self._method and self._params:
            self._method(**self._params)
        elif self._method:
            self._method()

    def set_args_and_start(self, **kwargs):
        self._params = kwargs
        self.start()


def print_something(range_input):
    for i in range(range_input):
        print(f"Data {i}")


print("Started.....")
with SaasContext(tkey="tKey", method=print_something) as context:
    context.set_args_and_start(range_input=5)

print("Print 0 Inside...")
print("Print 1 Inside...")
print("Print 2 Inside...")
print("Print 3 Inside...")
print("Done.")
