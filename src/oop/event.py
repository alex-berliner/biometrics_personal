class Event():
    # time must be second-resolution epoch time
    def __init__(self, time, note):
        self.time = int(time)
        self.note = str(note)

    # overload to perform one-time processing after all data is collected
    def process(self):
        pass

    def __str__(self):
        return "%s: %s"%(self.time, self.note)
