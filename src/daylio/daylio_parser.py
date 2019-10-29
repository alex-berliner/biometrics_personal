import re
import sys
sys.path.insert(0, "src/oop")
from headache_event import *
from event import *
from daylio_event import *
from headache_daylio_event import *
sys.path.insert(0, "src/daylio")
from daylio_table import *

class DaylioParser():
    daylio_regex_headache = "headache (\\<?\\d(\\.?\\d)?)".lower()
    daylio_regex_neck     = "neck pain (\\<?\\d(\\.?\\d)?)".lower()
    daylio_text_new_scale = "start new headache scale"
    # drugs = ["aimovig", "tylenol", "maxalt", "caffiene", "advil", "gralise", "gabapentin"]
    def __init__(self):
        self.all_fields   = []

        self.headache     = []
        self.all_fields += [self.headache]

        self.took_meds    = []
        self.all_fields += [self.took_meds]

        self.migraine     = []
        self.all_fields += [self.migraine]

        self.mood         = []
        self.all_fields += [self.mood]

        self.stomach_pain = []
        self.all_fields += [self.stomach_pain]

        self.neck_pain    = []
        self.all_fields += [self.neck_pain]

        self.ate_food     = []
        self.all_fields += [self.ate_food]

        self.sick         = []
        self.all_fields += [self.sick]

        self.started_meds = []
        self.all_fields += [self.started_meds]

        self.stopped_meds = []
        self.all_fields += [self.stopped_meds]

        self.exercise     = []
        self.all_fields += [self.exercise]

        self.fatigue      = []
        self.all_fields += [self.fatigue]

        self.misc         = []
        self.all_fields += [self.misc]

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
                conv_date = int(int(daylio_entry.date_time)/1000)
                event = DaylioEvent(conv_date, note)

                # Special case for headaches: scale was switched from 1-10 to 0-5, must convert
                # old entries based on conversion date marker
                if self.daylio_text_new_scale == lnote:
                    # print(lnote)
                    # print("switch date is %s"%event.time)
                    HeadacheDaylioEvent.switch_time = conv_date
                elif re.match(self.daylio_regex_headache, lnote):
                    self.headache += [HeadacheDaylioEvent(conv_date, note)]
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

        # for h in self.headache:
        #     print(h)
        for fields in self.all_fields:
            for field in fields:
                field.process()
        return headache_list
