# convert my app databases into csv files containing different streams of biometric data
import sqlite3
import sys

sys.path.insert(0, "src/daylio")
from convert_daylio import *
sys.path.insert(0, "src/migraine_buddy")
from mbuddy_parser import *

def main():
    biometrics_context = BiometricsContext()
    convert_daylio(biometrics_context)
    # mbuddy = Mbuddy()
    # mbuddy.connect_and_parse()
    biometrics_conn = sqlite3.connect('biometrics.db')
    biometrics_conn.commit()
    biometrics_conn.close()

if __name__ == "__main__":
    main()
