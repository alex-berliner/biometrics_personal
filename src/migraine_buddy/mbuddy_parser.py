import re
import sys

sys.path.insert(0, "src/oop")
from headache_event import *
from event import *
# from headache_daylio_event import *

sys.path.insert(0, "src/migraine_buddy")
from daylio_table import *

class Mbuddy():
    # daylio_regex_headache = "headache (\\<?\\d(\\.?\\d)?)".lower()
    # daylio_regex_neck     = "neck pain (\\<?\\d(\\.?\\d)?)".lower()
    # daylio_text_new_scale = "start new headache scale"
    # drugs = ["aimovig", "tylenol", "maxalt", "caffiene", "advil", "gralise", "gabapentin"]

    def __init__(self):
        pass

    def connect_and_parse(self):
        conn = sqlite3.connect('data_backings/migraine_buddy/migraine.db')
        mb_cursor = conn.execute('SELECT painIntensity,startTime,endTime FROM migraineevent')
        for row in mb_cursor:
            print(row)
        conn.close()
