from datetime import datetime

import csv
import pandas as pd
# filename =
f = pd.read_csv("../biometrics_personal/data_backings/daylio_csv/daylio_export_2020_11_14.csv")
# print(f)
keep_col = ["full_date", "date", "time",  "note"]
new_f = f[keep_col]
new_f.to_csv("newFile.csv", index=False)
# print(new_f)
keywords = ["started", "administered", "stopped"]
bads = ["took", "headache", "had", "used"]
goods = ["aimovig"]
all_events = []
for i in range(len(new_f)):
    note = str(new_f["note"][i]).lower()
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
                # print((time, event))
                continue
        for good in goods:
            if good in event:
                all_events += [(dt_obj, event)]
                break
print(len(all_events))
for event in all_events:
    print(event)

stamps = [int(x[0].timestamp()) for x in all_events]
events = [x[1] for x in all_events]

med_changes =  {"time": stamps,
                "med_events": events
                }
df = pd.DataFrame(med_changes, columns= ["time", "med_events"])

df.to_csv("/home/alex/bbbbb/biometrics/data/med_events.csv", index = False, header=True)
