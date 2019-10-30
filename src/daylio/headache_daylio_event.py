import re
import sys
sys.path.insert(0, "src/oop")
from event import *

# Different types
class HeadacheDaylioEvent(Event):
    switch_time = None

    daylio_regex_headache = "Headache (\\<?\\d(\\.\\d*)?)"
    def __init__(self, time, note):
        parent=super(HeadacheDaylioEvent, self)
        parent.__init__(time, note)
        self.intensity = None

    # Scale old headache scale (0-10) to new headache scale (0-5)
    def scale(self, intensity):
        scale = [ [5,5], [3,4], [2,3], [1,2], [0,1], [-1,0] ]
        for s in scale:
            if intensity > s[0]:
                return s[1]

    # convert headache data into new format
    def process(self):
        if self.switch_time is None:
            print("Headache switch time was not set!")
            exit()
        intensity_regex = re.match(self.daylio_regex_headache, self.note)
        if not intensity_regex:
            print("Encountered bad headache event: %s"%self)
            exit()
        intensity_raw = float(intensity_regex.group(1).replace("<1","0.5"))
        self.intensity = self.scale(intensity_raw) if (self.switch_time > self.time) else float(intensity_raw)
