# convert my daylio into csv files containing different streams of biometric data
import sys
import re
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, "../util/database")
from database import *

sys.path.insert(0, "src/oop")
from headache_event import *
from event import *

sys.path.insert(0, "src/daylio")
from daylio_table import *
from daylio_parser import *

daylio_regex_headache = "headache (\\<?\\d(\\.?\\d)?)".lower()
daylio_regex_neck     = "neck pain (\\<?\\d(\\.?\\d)?)".lower()
daylio_text_new_scale = "Start new head ache scale"
drugs = ["aimovig", "tylenol", "maxalt", "caffiene", "advil", "gralise", "gabapentin"]

    # for row in main_entries:
    #     te = HeadacheEvent()
    #     te.start  = datetime.fromtimestamp(int(row[0])/1000)
    #     te.notes = row[1].split("\n")

    #     # find medications taken
    #     for note_elem in te.notes:
    #         lowered_note = note_elem.lower()
    #         if "took" in lowered_note:
    #             for drug in drugs:
    #                 if drug in lowered_note:
    #                     te.meds += [drug]

    #         match = re.search(daylio_regex_neck, lowered_note)
    #         if match is not None:
    #             te.intensity_neck = str(match.group(1))

    #         match = re.search(daylio_regex_headache, lowered_note)
    #         if match is not None:
    #             te.intensity_head = str(match.group(1))
    #     if    te.intensity_neck is not None \
    #        or te.intensity_head is not None \
    #        or len(te.meds) > 0:
    #         headache_list += [te]

def main():
    biometrics_conn = sqlite3.connect('biometrics.db')
    daylio_conn     = sqlite3.connect('data_backings/daylio/entries.db')
    # parse_daylio(daylio_conn, [])
    daylio_parser = DaylioParser()
    daylio_parser.parse_daylio(daylio_conn, [])
    biometrics_conn.commit()
    biometrics_conn.close()
    daylio_conn.close()

if __name__ == "__main__":
    main()
