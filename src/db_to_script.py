import sys
sys.path.insert(0, "../database_util")
import sqlite3
import os
from database import *

class DatabaseScriptConverter:
    def __init__(self, path, dbname, scriptname):
        path = path.rstrip("/")
        self.dbpath     = "%s/%s"%(path, dbname)
        self.scriptpath = "%s/%s"%(path, scriptname)

    def save_sql_script(self):
        if not os.path.exists(self.dbpath):
            print(self.dbpath + " does not exist")
            return
        conn = sqlite3.connect(self.dbpath) # TODO check path exists
        with open(self.scriptpath, "w") as f:
            for line in conn.iterdump():
                f.write("%s\n" % line)
        conn.close()

database_migraine_buddy = DatabaseScriptConverter("databases/migraine_buddy", "migraine.db",        "migraine_buddy.sql")
database_daylio         = DatabaseScriptConverter("databases/daylio",         "entries.db",         "daylio.sql")
database_withings       = DatabaseScriptConverter("databases/withings",       "room-healthmate.db", "withings.sql")
dbs = \
[
    database_migraine_buddy,
    database_daylio,
    database_withings,
]

def convert_databases():
    for db in dbs:
        db.save_sql_script()

def main():
    convert_databases()

if __name__ == "__main__":
    main()
