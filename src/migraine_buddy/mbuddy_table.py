from enum import IntEnum
import sys
sys.path.insert(0, "../util/database")
from database import *

# CREATE TABLE table_entries (
# id INTEGER PRIMARY KEY AUTOINCREMENT
# minute INTEGER
# hour INTEGER
# day INTEGER
# month INTEGER
# year INTEGER
# date_time INTEGER
# time_zone_offset INTEGER
# mood INTEGER
# note TEXT

class DaylioEntry():
    class DaylioFields(IntEnum):
        ID = 0
        MINUTE = 1
        HOUR = 2
        DAY = 3
        MONTH = 4
        YEAR = 5
        DATE_TIME = 6
        TIME_ZONE_OFFSET = 7
        MOOD = 8
        NOTE = 9
    def __init__(self, daylio_tuple):
        self.id = daylio_tuple[self.DaylioFields.ID]
        self.minute = daylio_tuple[self.DaylioFields.MINUTE]
        self.hour = daylio_tuple[self.DaylioFields.HOUR]
        self.day = daylio_tuple[self.DaylioFields.DAY]
        self.month = daylio_tuple[self.DaylioFields.MONTH]
        self.year = daylio_tuple[self.DaylioFields.YEAR]
        self.date_time = daylio_tuple[self.DaylioFields.DATE_TIME]
        self.time_zone_offset = daylio_tuple[self.DaylioFields.TIME_ZONE_OFFSET]
        self.mood = daylio_tuple[self.DaylioFields.MOOD]
        self.note = daylio_tuple[self.DaylioFields.NOTE]

class DaylioTable(DBTable):
    def __init__(self):
        self.TABLE_NAME  = "DAYLIO_ENTRIES"
        fields = [\
            # Auction scan counter
            DBField("DATE",   "INTEGER", True),
            DBField("NOTE",   "TEXT",    False),
        ]
        parent=super(DaylioTable, self)
        parent.__init__(self.TABLE_NAME, fields)
