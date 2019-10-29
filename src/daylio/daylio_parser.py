import sys
sys.path.insert(0, "src/oop")
from headache_event import *
from event import *
sys.path.insert(0, "src/daylio")
from daylio_table import *

class DaylioParser():
    def __init__(self):
        self.headache     = []
        self.took_meds    = []
        self.migraine     = []
        self.mood         = []
        self.stomach_pain = []
        self.neck_pain    = []
        self.ate_food     = []
        self.sick         = []
        self.started_meds = []
        self.stopped_meds = []
        self.exercise     = []
        self.fatigue      = []
        self.misc         = []

    def parse_daylio(self, conn, headache_list):
        def sortkey(item): return item[0]

        cursor = conn.cursor()
        main_entries = cursor.execute('SELECT * FROM table_entries')
        main_entries = sorted(main_entries, key=sortkey)
        for row in main_entries:
            daylio_entry = DaylioEntry(row)
            notes = daylio_entry.note.split("\n")
            for note in notes:
                lnote = note.lower().strip()
                if len(lnote) < 1:
                    pass
                event = Event(daylio_entry.date_time, note)
                if "headache" in lnote:
                    self.headache += [event]
                elif "took" in lnote:
                    self.took_meds += [event]
                elif "migraine" in lnote:
                    self.migraine += [event]
                elif "mood" in lnote:
                    self.mood += [event]
                elif "stomach" in lnote:
                    self.stomach_pain += [event]
                elif "neck" in lnote:
                    self.neck_pain += [event]
                elif "ate " in lnote:
                    self.ate_food += [event]
                elif "sick" in lnote:
                    self.sick += [event]
                elif "started" in lnote:
                    self.started_meds += [event]
                elif "stopped" in lnote:
                    self.stopped_meds += [event]
                elif "exercise" in lnote\
                or "yoga" in lnote\
                or "soccer" in lnote\
                or "basketball" in lnote\
                or "snorkel" in lnote\
                or "bike" in lnote\
                or "elliptical" in lnote\
                or "walk" in lnote\
                or "hike" in lnote\
                    :
                    self.exercise += [event]
                elif "sleepy" in lnote\
                or "tired" in lnote\
                :
                    self.fatigue += [event]
                else:
                    self.misc += [event]
        return headache_list
