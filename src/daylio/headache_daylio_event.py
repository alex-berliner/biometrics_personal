import re
import sys
sys.path.insert(0, "src/oop")
from daylio_event import *

class HeadacheDaylioEvent(DaylioEvent):
    switch_time = None
    def scale(self, intensity):
        scale = [ [5,5], [3,4], [2,3], [1,2], [0,1], [-1,0] ]
        for s in scale:
            if intensity > s[0]:
                return s[1]

            # self.intensity_head = scale(float(self.intensity_head.replace("<1","0.5")))
    daylio_regex_headache = "Headache (\\<?\\d(\\.\\d*)?)"
    def __init__(self, time, note):
        parent=super(HeadacheDaylioEvent, self)
        parent.__init__(time, note)

    def process(self):
        # print(self.daylio_regex_headache)
        # exit()
        if self.switch_time is None:
            print("Headache switch time was not set!")
            exit()
        intensity_regex = re.match(self.daylio_regex_headache, self.note)
        if not intensity_regex:
            print("Encountered bad headache event: %s"%self)
            exit()
        intensity_raw = float(intensity_regex.group(1).replace("<1","0.5"))
        self.intensity = self.scale(intensity_raw) if (self.switch_time > self.time) else float(intensity_raw)
        print("%-35s %-20s %-20s %s"%(self, intensity_raw, self.intensity, self.switch_time > self.time))
        # exit()
