class App:

    request = None

    @classmethod
    def clean_up(cls):
        cls.request = None