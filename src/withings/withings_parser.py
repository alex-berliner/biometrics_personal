import re
import sys

sys.path.insert(0, "src/oop")
from headache_event import *
from event import *
# from headache_daylio_event import *

sys.path.insert(0, "src/withings")
from withings_table import *

class WithingsParser():
    def __init__(self):
        pass

    def connect_and_parse(self):
        conn = sqlite3.connect("data_backings/withings/room-healthmate.db")
        wi_cursor = conn.execute("SELECT * FROM Track")
        withings_entries = []
        for row in wi_cursor:
            withings_entry = WithingsEntry(row)
            withings_entries += [withings_entry]
            print(withings_entry)
            exit()
        conn.close()
