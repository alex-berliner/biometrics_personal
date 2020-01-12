from datetime import datetime, timedelta

class Event():
    def __init__(self, start, note, end=None):
        self.start    = start
        self.end      = end
        self.note     = note

    def __eq__(self, other):
        return self.start == other.start

    def __lt__(self, other):
        return self.start < other.start

    def __str__(self):
        retstr = ""
        return retstr.rstrip("\n")
