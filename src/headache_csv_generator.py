# convert my daylio data into csv files of related biometrics
import sys
sys.path.insert(0, "../util/database")
import sqlite3
import os
from database import *

def main():
    # reinflate daylio db
    conn = sqlite3.connect('temp_db_daylio.db')
    daylio_script = open("data_backings/daylio/daylio.sql").read()
    conn.executescript(daylio_script)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
