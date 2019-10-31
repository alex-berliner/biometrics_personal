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
        wi_db = list(conn.execute("SELECT * FROM Track"))

        withings_entries = []
        for i in range(len(wi_db)):
        # for row in wi_cursor:
            row = wi_db[i]
            withings_entry = WithingsEntry(row)
            withings_entries += [withings_entry]
            sleep_time = withings_entry.get_sleep_time()
            # if sleep_time > 0:
            #     print(sleep_time)
            # if i > 0:
            #     exit()
        # print(WithingsEntry.typesdict.keys())
        conn.close()
