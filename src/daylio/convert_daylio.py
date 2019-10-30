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

def convert_daylio(biometrics_context):
    daylio_parser = DaylioParser()
    daylio_conn = sqlite3.connect('data_backings/daylio/entries.db')
    daylio_parser.parse_daylio(daylio_conn, biometrics_context)
    daylio_conn.close()

def main():
    convert_daylio()

if __name__ == "__main__":
    main()
