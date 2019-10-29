import re
import sys

sys.path.insert(0, "src/oop")
from headache_event import *
from event import *
from daylio_event import *
from headache_daylio_event import *

sys.path.insert(0, "src")
from parser import *

sys.path.insert(0, "src/daylio")
from daylio_table import *

class DaylioParser():
    daylio_regex_headache = "headache (\\<?\\d(\\.?\\d)?)".lower()
    daylio_regex_neck     = "neck pain (\\<?\\d(\\.?\\d)?)".lower()
    daylio_text_new_scale = "start new headache scale"
    # drugs = ["aimovig", "tylenol", "maxalt", "caffiene", "advil", "gralise", "gabapentin"]

    def __init__(self):
        parent=super(DaylioParser, self)
        parent.__init__()

    def parse_daylio(self, conn):
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
                    Parser.headache += [HeadacheDaylioEvent(conv_date, note)]
                elif "took" in lnote:
                    Parser.took_meds += [event]
                elif "migraine" in lnote:
                    Parser.migraine += [event]
                elif "mood" in lnote:
                    Parser.mood += [event]
                elif "stomach" in lnote:
                    Parser.stomach_pain += [event]
                elif "neck" in lnote:
                    Parser.neck_pain += [event]
                elif "ate " in lnote:
                    Parser.ate_food += [event]
                elif "sick" in lnote:
                    Parser.sick += [event]
                elif "started" in lnote:
                    Parser.started_meds += [event]
                elif "stopped" in lnote:
                    Parser.stopped_meds += [event]
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
                    Parser.exercise += [event]
                elif "sleepy" in lnote\
                or "tired" in lnote\
                :
                    Parser.fatigue += [event]
                else:
                    Parser.misc += [event]
