import sys
sys.path.insert(0, "../database_util")
import sqlite3
import os
from database import *

class DatabaseScriptConverter:
    def __init__(self, path, dbname, scriptname):
        path=path.rstrip("/")
        self.dbpath     = "%s/%s"%(path, dbname)
        self.scriptpath = "%s/%s"%(path, scriptname)

    def save_sql_script(self):
        conn = sqlite3.connect(self.dbpath) # TODO make sure path exists
        with open(self.scriptpath, "w") as f:
            for line in conn.iterdump():
                f.write("%s\n" % line)
        conn.close()

database_migraine_buddy = DatabaseScriptConverter("migraine_buddy", "migraine.db",        "migraine_buddy.sql")
database_daylio         = DatabaseScriptConverter("daylio",         "entries.db",         "daylio.sql")
database_withings       = DatabaseScriptConverter("withings",       "room-healthmate.db", "withings.sql")
dbs = \
[
    database_migraine_buddy,
    database_daylio,
    database_withings,
]

def main():
    for db in dbs:
        db.save_sql_script()

if __name__ == "__main__":
    main()
