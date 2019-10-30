# All events will be stored based on type (headache, migraine, etc), so parsers from all backends
# can share this common base to add to the shared event lists
class Parser():
    event_types   = []
    headache     = []
    took_meds    = []
    migraine     = []
    mood         = []
    stomach_pain = []
    neck_pain    = []
    ate_food     = []
    sick         = []
    started_meds = []
    stopped_meds = []
    exercise     = []
    fatigue      = []
    misc         = []
    event_types += [headache]
    event_types += [took_meds]
    event_types += [migraine]
    event_types += [mood]
    event_types += [stomach_pain]
    event_types += [neck_pain]
    event_types += [ate_food]
    event_types += [sick]
    event_types += [started_meds]
    event_types += [stopped_meds]
    event_types += [exercise]
    event_types += [fatigue]
    event_types += [misc]

    def __init__(self):
        pass

    def process_all(self):
        for event_list in Parser.event_types:
            for event in event_list:
                event.process()

