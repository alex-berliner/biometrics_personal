import re
import sys

sys.path.insert(0, "src/oop")
from headache_event import *
from sleep_table import *
# from headache_daylio_event import *

sys.path.insert(0, "src/withings")
from withings_table import *

class WithingsParser():
    def __init__(self):
        pass

    def connect_and_parse(self, biometrics_conn):
        sleep_table = SleepTable()
        healthmate_conn = sqlite3.connect("data_backings/withings/room-healthmate.db")
        track_table = list(healthmate_conn.execute("SELECT * FROM Track"))
        sleep_table.create_table(biometrics_conn)
        for i in range(len(track_table)):
            track_tuple = track_table[i]
            withings_sleep_entry = WithingsSleepEvent(track_tuple)
            if withings_sleep_entry.sleep:
                sleep_table.add_entry(biometrics_conn, withings_sleep_entry.to_db_tuple())

        # print(sleep_table.dump(biometrics_conn))
        healthmate_conn.close()

        # wiscale_conn = sqlite3.connect("data_backings/withings/Withings-WiScale.db")
        # timeline_table = list(wiscale_conn.execute("SELECT * FROM timeline"))
        # for i in range(len(timeline_table)):
        #     timeline_row = timeline_table[i]
        #     withings_entry = withings_table.add_entry(timeline_tuple=timeline_row)
        # #     withings_measure_tuple
        # wiscale_conn.close()

