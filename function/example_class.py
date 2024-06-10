class ExampleClass:

    def print_something(self, first_name: str, last_name: str, **kwargs):
        print(f'{first_name} {last_name}')
        print(kwargs)


example = ExampleClass()
params = {"first_name": "John", "last_name": "Doe", "other": "worker"}
example.print_something(**params)
