import sys
sys.path.insert(0, "../utils/database")
from database import *

class SleepTable(DBTable):
    def __init__(self):
        self.TABLE_NAME  = "Sleep"
        fields = [\
            DBField("WAKEUP_YYYYMMDD", "TEXT",    True),
            DBField("START_EPOCH",     "INTEGER", False),
            DBField("END_EPOCH",       "INTEGER", False),
            DBField("SLEPT_TIME_S",    "INTEGER", False),
        ]
        parent=super(SleepTable, self)
        parent.__init__(self.TABLE_NAME, fields)
