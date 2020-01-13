import csv

# Data holder to be added to by all data backends
class BiometricsContext():
    def __init__(self):
        # create categories of tracked data
        self.headache     = []
        self.took_meds    = []
        self.migraine     = []
        self.mood         = []
        self.stomach_pain = []
        self.neck_pain    = []
        self.ate_food     = []
        self.sick         = []
        self.started_meds = []
        self.stopped_meds = []
        self.exercise     = []
        self.fatigue      = []
        self.misc         = []

        # add all categories to one list so they can be looped through
        self.event_types  = []
        self.event_types += [self.headache]
        self.event_types += [self.took_meds]
        self.event_types += [self.migraine]
        self.event_types += [self.mood]
        self.event_types += [self.stomach_pain]
        self.event_types += [self.neck_pain]
        self.event_types += [self.ate_food]
        self.event_types += [self.sick]
        self.event_types += [self.started_meds]
        self.event_types += [self.stopped_meds]
        self.event_types += [self.exercise]
        self.event_types += [self.fatigue]
        self.event_types += [self.misc]

    def process_all(self):
        for event_list in self.event_types:
            for event in event_list:
                event.process()

    def output_headache_csv(self, outpath):
        writepath = outpath + "headache.csv"
        csvfile = open(writepath, "w", newline='')
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_lines = []
        for headache_event in self.headache:
            headache_event.process()
            csv_lines += [headache_event.to_csv()]
        csv_lines.sort()
        spamwriter.writerow(["time", "rating"])
        for line in csv_lines:
            spamwriter.writerow(line)

    def output_meds_csv(self, outpath):
        writepath = outpath + "medicine.csv"
        csvfile = open(writepath, "w", newline='')
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(["time", "medication"])

        types = {}
        csv_lines = []

        for med_event in self.took_meds:
            csv_lines += [med_event.to_csv()]
            if med_event.note not in types:
                types[med_event.note] = 0
            types[med_event.note] += 1

        csv_lines.sort()

        for line in csv_lines:
            spamwriter.writerow(line)
