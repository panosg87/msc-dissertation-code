class BaseCriteria:

    def __init__(self, durations):
        try:
            self.name = self.__doc__.split('Algorithm')[0].strip()
        except:
            self.name = None
        self.durations = durations
