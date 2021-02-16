

class Bismillah:

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        pass

    # @property
    def print_me(self):
        print("Bismillah")
        return "Flask Extension Bismillah"
