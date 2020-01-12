sys.path.insert(0, "../utils/database")
from database import *

class HeartTable(DBTable):
    def __init__(self):
        self.TABLE_NAME  = "HEART"
        fields = [\
            DBField("START_EPOCH", "INTEGER", False),
            DBField("SYSTOLIC",    "INTEGER", False),
            DBField("DIASTOLIC",   "INTEGER", False),
            DBField("HEARTRATE",   "INTEGER", False),
        ]
        parent=super(HeartTable, self)
        parent.__init__(self.TABLE_NAME, fields)
