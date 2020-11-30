import re
from datetime import datetime
import csv
import pandas as pd
import os

def headache_scale(intensity):
    mapping = [ [5,5], [3,4], [2,3], [1,2], [0,1], [-1,0] ]
    for s in mapping:
        if intensity > s[0]:
            return s[1]

files = os.listdir(os.environ["HOME"] + "/downloads")
myfile = os.environ["HOME"] + "/downloads/" + sorted([x for x in files if re.match(".*\.csv", x)])[-1]
print("Reading %s"%myfile)
f = pd.read_csv(myfile)
keep_col = ["full_date", "date", "time",  "note"]
new_f = f[keep_col]
keywords = ["started", "ended", "administered", "stopped", "performed"]
bads = ["took", "headache", "had", "used"]
goods = ["aimovig"]
all_events = []
headache_events = []
headache_scale_switch=datetime.fromtimestamp(1541430000)

for i in range(len(new_f)):
    note = str(new_f["note"][i]).lower().replace("administered", "performed")
    events = []
    for keyword in keywords+bads:
        note = note.replace(" %s"%keyword, ";%s"%keyword)
    events = note.split(";")
    time = "%s %s"%(new_f["full_date"][i], new_f["time"][i])
    dt_obj = datetime.strptime(time, "%Y-%m-%d %I:%M %p")
    for event in events:
        for keyword in keywords:
            if keyword in event:
                all_events += [(dt_obj, event)]
                continue
        for good in goods:
            if good in event:
                all_events += [(dt_obj, event)]
                break
    for event in events:
        if "headache" in event:
            mmm = re.findall(".*[Hh]eadache (\d(\.\d*)?).*", event)
            if len(mmm) > 0:
                intensity = float(mmm[0][0])

                # Special case for headaches: scale was switched from 1-10 to 0-5, must convert
                # old entries based on conversion date marker
                if headache_scale_switch > dt_obj:
                    intensity = headache_scale(intensity)

                qol = 100.0 - 20 * intensity
                headache_events += [(dt_obj, qol)]

med_stamps = [int(x[0].timestamp()) for x in all_events]
med_events = [x[1] for x in all_events]
med_changes =  {"time": med_stamps, "med_events": med_events }
med_df = pd.DataFrame(med_changes, columns= ["time", "med_events"])
med_df.to_csv(os.environ["BIOMETRICS_ROOT"] + "/biometrics/data/med_events.csv", index=False, header=True)

headache_events.reverse()
headache_stamps = [int(x[0].timestamp()) for x in headache_events]
headache_events = [x[1] for x in headache_events]
headache_changes =  {"time": headache_stamps, "rating": headache_events }
headache_df = pd.DataFrame(headache_changes, columns= ["time", "rating"])
headache_df.to_csv(os.environ["BIOMETRICS_ROOT"] + "/biometrics/data/headache.csv", index=False, header=True)
