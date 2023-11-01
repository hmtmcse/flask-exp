class Helper:
    def print_data(self):
        print("Print Data")


class CRUDCommon:
    model: str = None
    helper: Helper = Helper()


class Child(CRUDCommon):

    def __init__(self):
        self.model = "Model"

    def print(self):
        self.helper.print_data()


Child().print()
