import sys
sys.path.insert(0, "../utils")

import time_util
import re

# Different types
class MedicationEvent():
    def __init__(self, time, note):
        self.time = time
        self.note = note
        if self.note == "aimovig":
            if self.time > 1552136459:
                self.note = "aimovig 140mg"
            else:
                self.note = "aimovig 70mg"
        self.note=self.note\
            .replace("1 tylenol", "tylenol")\
            .replace("maxalt 10mg", "maxalt")\
            .replace("caffeine 200mg", "maxalt")\
            .replace("caffeine 100mg", "caffeine")\
            .replace("aimovig 140 mg", "aimovig 140mg")\
            .replace("aimovig 70 mg", "aimovig 70mg")\
            .replace("second maxalt", "maxalt")\
            .replace("sumatriptan injectable 3mg", "sumatriptan injectable")\
            .replace("tylenol 500mg", "tylenol")\
            .replace("tylenol 500 mg", "tylenol")\
# 1552136459
    def __str__(self):
        return "%s: %s"%(time_util.epoch_to_yyyy_mm_dd(self.time), self.note)

    def to_csv(self):
        return (self.time, self.note)

    # convert headache data into new format
    def process(self):
        return
