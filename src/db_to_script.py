import sys
sys.path.insert(0, "../utils/database")
import sqlite3
import os
from database import *

class DatabaseScriptConverter:
    def __init__(self, path, db_name, saved_name):
        path = path.rstrip("/")
        self.saved_name = saved_name
        self.db_path  = "%s/%s"%(path, db_name)
        self.script_path = "%s/%s.sql"%(path, saved_name)

    def sql_script_save(self):
        if not os.path.exists(self.db_path):
            return False

        # perform dump with system command
        os.system("sqlite3 %s .dump > %s"%(self.db_path, self.script_path))

        # This should work but there's a bug in the current implementation of sqlite for python
        # that causes the output to be unusable
        # https://bugs.python.org/issue34828
        # https://github.com/python/cpython/pull/9621
        # conn = sqlite3.connect(self.db_path) # TODO check path exists
        # with open(self.script_path, "w") as f:
        #     for line in conn.iterdump():
        #         f.write("%s\n" % line)
        # conn.close()

        return True

    def sql_script_load(self):
        if not os.path.exists(self.script_path):
            return False

        os.system("sqlite3 %s < %s"%(self.db_path, self.script_path))

        return True


database_migraine_buddy = DatabaseScriptConverter("data_backings/migraine_buddy", "migraine.db",        "migraine_buddy")
database_daylio         = DatabaseScriptConverter("data_backings/daylio",         "entries.db",         "daylio")
database_withings       = DatabaseScriptConverter("data_backings/withings",       "room-healthmate.db", "withings")
database_withings       = DatabaseScriptConverter("data_backings/withings",       "androidx.work.workdb", "androidx.work.workdb")
database_withings       = DatabaseScriptConverter("data_backings/withings",       "google_app_measurement_local.db", "google_app_measurement_local.db")
database_withings       = DatabaseScriptConverter("data_backings/withings",       "Withings-WiScale", "Withings-WiScale")

dbs = \
[
    database_migraine_buddy,
    database_daylio,
    database_withings,
]

def convert_databases():
    # convert the current database to a script
    # if the database doesn't exist, repopulate it from the script
    for db in dbs:
        if not db.sql_script_save():
            if not db.sql_script_load():
                print("Both database and script for %s are missing."%(db.saved_name))

def main():
    convert_databases()

if __name__ == "__main__":
    main()
