# convert my daylio into csv files containing different streams of biometric data
import sys
import re
import sqlite3
from datetime import datetime, timedelta

sys.path.insert(0, "../util/database")
from database import *

sys.path.insert(0, "src/oop")
from headache_event import *
from event import *

sys.path.insert(0, "src/daylio")
from daylio_table import *
from daylio_parser import *

sys.path.insert(0, "src")
from parser import *

def main():
    biometrics_conn = sqlite3.connect('biometrics.db')
    daylio_conn     = sqlite3.connect('data_backings/daylio/entries.db')
    daylio_parser = DaylioParser()
    daylio_parser.parse_daylio(daylio_conn)

    parser = Parser()
    parser.process_all()

    biometrics_conn.commit()
    biometrics_conn.close()
    daylio_conn.close()

if __name__ == "__main__":
    main()
