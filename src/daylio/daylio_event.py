import sys
sys.path.insert(0, "src/oop")
from event import *

class DaylioEvent(Event):
    def __init__(self, time, note):
        parent=super(DaylioEvent, self)
        parent.__init__(time, note)
