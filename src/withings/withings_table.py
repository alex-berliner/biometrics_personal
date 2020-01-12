from collections import OrderedDict
from datetime import timedelta
from enum import IntEnum
import json
import sys
import time

sys.path.insert(0, "../utils")
import time_util

sys.path.insert(0, "../utils/database")
from database import *

sys.path.insert(0, "src/oop")
from sleep_event import *
from sleep_table import *

class WithingsSleepEvent(SleepEvent):
    class WithingsTrackFields(IntEnum):
        ID=0
        WSID=1
        USERID=2
        STARTDATE=3
        ENDDATE=4
        TIMEZONE=5
        DAY=6
        MODIFIEDDATE=7
        DEVICEMODEL=8
        DEVICETYPE=9
        ATTRIB=10
        CATEGORY=11
        DATAJSON=12
        ACTIVITYRECOGNITIONVERSION=13
        ISSYNCEDTOWS=14
        DELETED=15
        DELETIONREASON=16
        NOTE=17
        SNORINGENABLED=18
        INPROGRESS=19
        MANUALSTARTDATE=20
        MANUALENDDATE=21
        BLANKVASISTASFILLED=22
        PATHLISTS=23
        CRYPTPART=24
        COVERPICTUREURL=25
        URIS=26
        COVERPICTUREURI=27
        SLEEPSCOREVALUE=28
        SLEEPSCORESTATUS=29
        SLEEPSCOREALGOVERSION=30
        DURATION_INFO_SCORE=31
        DURATION_INFO_STATUS=32
        RECOVERY_INFO_SCORE=33
        RECOVERY_INFO_STATUS=34
        INTERRUPTIONS_INFO_SCORE=35
        INTERRUPTIONS_INFO_STATUS=36
        TIMETOFALLASLEEP_INFO_SCORE=37
        TIMETOFALLASLEEP_INFO_STATUS=38
        TIMETOWAKEUP_INFO_SCORE=39
        TIMETOWAKEUP_INFO_STATUS=40
        REGULARITY_INFO_SCORE=41
        REGULARITY_INFO_STATUS=42
        SNORING_INFO_SCORE=43
        SNORING_INFO_STATUS=44
        NIGHT_HEARTRATE_INFO_SCORE=45
        NIGHT_HEARTRATE_INFO_STATUS=46
        DISTANCE=47
        AVERAGESPEED=48
        MINSPEED=49
        MAXSPEED=50
        STARTLATITUDE=51
        STARTLONGITUDE=52
        ENDLATITUDE=53
        ENDLONGITUDE=54
        CENTERLATITUDE=55
        CENTERLONGITUDE=56
        SPANLATITUDEDELTA=57
        SPANLONGITUDEDELTA=58

    def set_fields_from_track_tuple(self, track_tuple):
        # TODO there has to be a better way to do this
        self.id=track_tuple[self.WithingsTrackFields.ID]
        self.wsid=track_tuple[self.WithingsTrackFields.WSID]
        self.userid=track_tuple[self.WithingsTrackFields.USERID]
        self.startdate=track_tuple[self.WithingsTrackFields.STARTDATE]
        self.enddate=track_tuple[self.WithingsTrackFields.ENDDATE]
        self.timezone=track_tuple[self.WithingsTrackFields.TIMEZONE]
        self.day=track_tuple[self.WithingsTrackFields.DAY]
        self.modifieddate=track_tuple[self.WithingsTrackFields.MODIFIEDDATE]
        self.devicemodel=track_tuple[self.WithingsTrackFields.DEVICEMODEL]
        self.devicetype=track_tuple[self.WithingsTrackFields.DEVICETYPE]
        self.attrib=track_tuple[self.WithingsTrackFields.ATTRIB]
        self.category=track_tuple[self.WithingsTrackFields.CATEGORY]
        self.datajson=track_tuple[self.WithingsTrackFields.DATAJSON]
        self.activityrecognitionversion=track_tuple[self.WithingsTrackFields.ACTIVITYRECOGNITIONVERSION]
        self.issyncedtows=track_tuple[self.WithingsTrackFields.ISSYNCEDTOWS]
        self.deleted=track_tuple[self.WithingsTrackFields.DELETED]
        self.deletionreason=track_tuple[self.WithingsTrackFields.DELETIONREASON]
        self.note=track_tuple[self.WithingsTrackFields.NOTE]
        self.snoringenabled=track_tuple[self.WithingsTrackFields.SNORINGENABLED]
        self.inprogress=track_tuple[self.WithingsTrackFields.INPROGRESS]
        self.manualstartdate=track_tuple[self.WithingsTrackFields.MANUALSTARTDATE]
        self.manualenddate=track_tuple[self.WithingsTrackFields.MANUALENDDATE]
        self.blankvasistasfilled=track_tuple[self.WithingsTrackFields.BLANKVASISTASFILLED]
        self.pathlists=track_tuple[self.WithingsTrackFields.PATHLISTS]
        self.cryptpart=track_tuple[self.WithingsTrackFields.CRYPTPART]
        self.coverpictureurl=track_tuple[self.WithingsTrackFields.COVERPICTUREURL]
        self.uris=track_tuple[self.WithingsTrackFields.URIS]
        self.coverpictureuri=track_tuple[self.WithingsTrackFields.COVERPICTUREURI]
        self.sleepscorevalue=track_tuple[self.WithingsTrackFields.SLEEPSCOREVALUE]
        self.sleepscorestatus=track_tuple[self.WithingsTrackFields.SLEEPSCORESTATUS]
        self.sleepscorealgoversion=track_tuple[self.WithingsTrackFields.SLEEPSCOREALGOVERSION]
        self.duration_info_score=track_tuple[self.WithingsTrackFields.DURATION_INFO_SCORE]
        self.duration_info_status=track_tuple[self.WithingsTrackFields.DURATION_INFO_STATUS]
        self.recovery_info_score=track_tuple[self.WithingsTrackFields.RECOVERY_INFO_SCORE]
        self.recovery_info_status=track_tuple[self.WithingsTrackFields.RECOVERY_INFO_STATUS]
        self.interruptions_info_score=track_tuple[self.WithingsTrackFields.INTERRUPTIONS_INFO_SCORE]
        self.interruptions_info_status=track_tuple[self.WithingsTrackFields.INTERRUPTIONS_INFO_STATUS]
        self.timetofallasleep_info_score=track_tuple[self.WithingsTrackFields.TIMETOFALLASLEEP_INFO_SCORE]
        self.timetofallasleep_info_status=track_tuple[self.WithingsTrackFields.TIMETOFALLASLEEP_INFO_STATUS]
        self.timetowakeup_info_score=track_tuple[self.WithingsTrackFields.TIMETOWAKEUP_INFO_SCORE]
        self.timetowakeup_info_status=track_tuple[self.WithingsTrackFields.TIMETOWAKEUP_INFO_STATUS]
        self.regularity_info_score=track_tuple[self.WithingsTrackFields.REGULARITY_INFO_SCORE]
        self.regularity_info_status=track_tuple[self.WithingsTrackFields.REGULARITY_INFO_STATUS]
        self.snoring_info_score=track_tuple[self.WithingsTrackFields.SNORING_INFO_SCORE]
        self.snoring_info_status=track_tuple[self.WithingsTrackFields.SNORING_INFO_STATUS]
        self.night_heartrate_info_score=track_tuple[self.WithingsTrackFields.NIGHT_HEARTRATE_INFO_SCORE]
        self.night_heartrate_info_status=track_tuple[self.WithingsTrackFields.NIGHT_HEARTRATE_INFO_STATUS]
        self.distance=track_tuple[self.WithingsTrackFields.DISTANCE]
        self.averagespeed=track_tuple[self.WithingsTrackFields.AVERAGESPEED]
        self.minspeed=track_tuple[self.WithingsTrackFields.MINSPEED]
        self.maxspeed=track_tuple[self.WithingsTrackFields.MAXSPEED]
        self.startlatitude=track_tuple[self.WithingsTrackFields.STARTLATITUDE]
        self.startlongitude=track_tuple[self.WithingsTrackFields.STARTLONGITUDE]
        self.endlatitude=track_tuple[self.WithingsTrackFields.ENDLATITUDE]
        self.endlongitude=track_tuple[self.WithingsTrackFields.ENDLONGITUDE]
        self.centerlatitude=track_tuple[self.WithingsTrackFields.CENTERLATITUDE]
        self.centerlongitude=track_tuple[self.WithingsTrackFields.CENTERLONGITUDE]
        self.spanlatitudedelta=track_tuple[self.WithingsTrackFields.SPANLATITUDEDELTA]
        self.spanlongitudedelta=track_tuple[self.WithingsTrackFields.SPANLONGITUDEDELTA]
        self.datajson_parsed = json.loads(self.datajson)
    def parse_fields_from_track_tuple(self, track_tuple):
        def to_timedelta(key):
            if key in self.datajson_parsed:
                return timedelta(seconds=(int(self.datajson_parsed[key])/1000))
            else:
                return timedelta(0)
        self.sleep = False

        self.set_fields_from_track_tuple(track_tuple)

        sleep_sum = 0
        if "lightSleepDuration" in self.datajson_parsed:
            sleep_sum += int(self.datajson_parsed["lightSleepDuration"])

        if "deepSleepDuration" in self.datajson_parsed:
            sleep_sum += int(self.datajson_parsed["deepSleepDuration"])

        if "manualSleepDuration" in self.datajson_parsed:
            sleep_sum += int(self.datajson_parsed["manualSleepDuration"])


        if sleep_sum > 0:
            self.sleep = True
            self.light_sleep_duration  = to_timedelta("lightSleepDuration")
            self.deep_sleep_duration   = to_timedelta("deepSleepDuration")
            self.manual_sleep_duration = to_timedelta("manualSleepDuration")
            self.rem_sleep_duration    = to_timedelta("remSleepDuration")

            self.sleep_start = int(self.startdate)/1000
            self.sleep_end = int(self.enddate)/1000+self.manual_sleep_duration.seconds

            self.timedelta_in_bed = timedelta(seconds=(self.sleep_end-self.sleep_start))
            self.timedelta_slept = self.manual_sleep_duration + self.light_sleep_duration + self.deep_sleep_duration + self.rem_sleep_duration

    def __init__(self, track_tuple):
        self.parse_fields_from_track_tuple(track_tuple)
        if self.sleep:
            parent=super(WithingsSleepEvent, self)
            parent.__init__(self.sleep_start, self.sleep_end, self.timedelta_slept)

    def get_yyyymmdd(self):
        return time_util.epoch_to_yyyymmdd(self.enddate)

class WithingsEntry():
    class WithingsTimelineFields(IntEnum):
        ID = 0
        USER = 1
        TIMESTAMP = 2
        TYPE = 3
        CUSTOMID = 4
        DATA = 5
        DELETED = 6
        EXPIRATIONDATE = 7
        SECTIONTAGS = 8

    def set_fields_from_timeline_tuple(self, timeline_tuple):
        pass

    def parse_fields_from_timeline_tuple(self, timeline_tuple):
        self.set_fields_from_timeline_tuple(timeline_tuple)
        ID = 0 # 28,
        USER = 1 # 19711056,
        TIMESTAMP = 2 # 1571509180000,
        TYPE = 3 # 'measure',
        CUSTOMID = 4 # '7',
        DATA = 5 # '{"measureGroupId":15,"measures":[{"y":93.0,"type":9},{"y":125.0,"type":10},{"y":93.0,"type":11}]}'
        DELETED = 6 # 0,
        EXPIRATIONDATE = 7 # 0,
        SECTIONTAGS = 8 # ''


    def __init__(self, timeline_tuple=None):
        if timeline_tuple:
            self.parse_fields_from_timeline_tuple(timeline_tuple)

    # def parse_track(self, )

    def __str__(self):
        pass


# class WithingsSleepTable(DBTable):
#     def __init__(self):
#         pass

# class WithingsHeartTable(DBTable):
#     def __init__(self):
#         self.TABLE_NAME  = "ENTRIES"
#         fields = [\
#             # Auction scan counter
#             DBField("ID",     "INTEGER", True),
#         ]
#         parent=super(WithingsTable, self)
#         parent.__init__(self.TABLE_NAME, fields)
#     def __init__(self):
#         self.TABLE_NAME  = "ENTRIES"
#         fields = [\
#             # Auction scan counter
#             DBField("ID",     "INTEGER", True),
#         ]
#         parent=super(WithingsTable, self)
#         parent.__init__(self.TABLE_NAME, fields)


# class WithingsTable(DBTable):
#     def __init__(self):
#         self.TABLE_NAME  = "ENTRIES"
#         fields = [\
#             # Auction scan counter
#             DBField("ID",     "INTEGER", True),
#         ]
#         parent=super(WithingsTable, self)
#         parent.__init__(self.TABLE_NAME, fields)

#         self.entries = {}

#     def add_entry(self, track_tuple=None, timeline_tuple=None):
#         if track_tuple:
#             entry = WithingsEntry(track_tuple=track_tuple)
#             date = entry.get_yyyymmdd()
#             if date not in self.entries:
#                 self.entries[date] = entry
#             else:
#                 entry = self.entries[date]
#                 entry.parse_fields_from_track_tuple(track_tuple)
#         if timeline_tuple:
#             entry = WithingsEntry(timeline_tuple=timeline_tuple)
#             date = entry.get_yyyymmdd()
#             if date not in self.entries:
#                 self.entries[date] = entry
#             else:
#                 entry = self.entries[date]
#                 entry.parse_fields_from_timeline_tuple(timeline_tuple)

#         return self.entries[date]
