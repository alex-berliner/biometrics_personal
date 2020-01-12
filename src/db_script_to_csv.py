# convert my app databases into csv files containing different streams of biometric data
import sqlite3
import sys

sys.path.insert(0, "src/oop")
from biometrics_context import *

sys.path.insert(0, "src/daylio")
from daylio_parser import *

sys.path.insert(0, "src/migraine_buddy")
from mbuddy_parser import *

sys.path.insert(0, "src/withings")
from withings_parser import *

def convert_daylio(biometrics_context):
    daylio_parser = DaylioParser()
    daylio_conn = sqlite3.connect('data_backings/daylio/entries.db')
    daylio_parser.parse_daylio(daylio_conn, biometrics_context)
    daylio_conn.close()

def main():
    biometrics_context = BiometricsContext()
    convert_daylio(biometrics_context)
    biometrics_context.output_headache_csv("../biometrics/data/")
    biometrics_context.output_meds_csv("../biometrics/data/")

    biometrics_conn = sqlite3.connect('biometrics.db')

    # TODO fix failure on finding Track field
    # wparser = WithingsParser()
    # wparser.connect_and_parse(biometrics_conn)

    biometrics_conn.commit()
    biometrics_conn.close()

if __name__ == "__main__":
    main()
