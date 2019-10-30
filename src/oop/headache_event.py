from datetime import datetime, timedelta

class HeadacheEvent():
    def __init__(self, start=None, intensity_head=None, intensity_neck=None):
        self.start          = start
        self.end            = None
        self.duration       = timedelta(0)
        self.intensity_head = intensity_head
        self.intensity_neck = intensity_neck
        self.notes          = ""
        self.meds           = []
        self.scale_switched = False

    def __eq__(self, other):
        return self.start == other.start

    def __lt__(self, other):
        return self.start < other.start

    def __str__(self):
        retstr = ""

        if self.end is None:
            self.end = self.start

        if self.intensity_head:
            retstr += "Head Intensity: " + str(self.intensity_head) + "\n"

        if self.intensity_neck:
            retstr += "Neck Intensity: " + str(self.intensity_neck) + "\n"

        if self.start:
            retstr += "Start: " + str(self.start) + "\n"

        if self.end:
            retstr += "End:   " + str(self.end) + "\n"

        if len(self.meds) > 0:
            retstr += "Meds:" + "\n"
            for med in self.meds:
                retstr += "\t" + med + "\n"

        return retstr.rstrip("\n")

    def scale_switch(self, switch_date):
        def scale(intensity):
            scale = [ [5,5], [3,4], [2,3], [1,2], [0,1], [-1,0] ]
            for s in scale:
                if intensity > s[0]:
                    return s[1]

        if self.scale_switched is True or switch_date is None:
            return

        self.scale_switched = True

        if (self.start - switch_date).total_seconds() > 0:
            return

        if self.intensity_head is not None:
            self.intensity_head = scale(float(self.intensity_head.replace("<1","0.5")))

        if self.intensity_neck is not None:
            self.intensity_neck = scale(float(self.intensity_neck.replace("<1","0.5")))
