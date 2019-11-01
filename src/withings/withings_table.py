import time
from enum import IntEnum
import sys
sys.path.insert(0, "../util")
import time_util
sys.path.insert(0, "../util/database")
from database import *
import json
from collections import OrderedDict
from datetime import timedelta
# CREATE TABLE table_entries (
# id INTEGER PRIMARY KEY AUTOINCREMENT
# minute INTEGER
# hour INTEGER
# day INTEGER
# month INTEGER
# year INTEGER
# date_time INTEGER
# time_zone_offset INTEGER
# mood INTEGER
# note TEXT

class WithingsEntry():
    class WithingsFields(IntEnum):
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

    def set_fields_from_tuple(self, withings_tuple):
        # TODO there has to be a better way to do this
        self.id=withings_tuple[self.WithingsFields.ID]
        self.wsid=withings_tuple[self.WithingsFields.WSID]
        self.userid=withings_tuple[self.WithingsFields.USERID]
        self.startdate=withings_tuple[self.WithingsFields.STARTDATE]
        self.enddate=withings_tuple[self.WithingsFields.ENDDATE]
        self.timezone=withings_tuple[self.WithingsFields.TIMEZONE]
        self.day=withings_tuple[self.WithingsFields.DAY]
        self.modifieddate=withings_tuple[self.WithingsFields.MODIFIEDDATE]
        self.devicemodel=withings_tuple[self.WithingsFields.DEVICEMODEL]
        self.devicetype=withings_tuple[self.WithingsFields.DEVICETYPE]
        self.attrib=withings_tuple[self.WithingsFields.ATTRIB]
        self.category=withings_tuple[self.WithingsFields.CATEGORY]
        self.datajson=withings_tuple[self.WithingsFields.DATAJSON]
        self.activityrecognitionversion=withings_tuple[self.WithingsFields.ACTIVITYRECOGNITIONVERSION]
        self.issyncedtows=withings_tuple[self.WithingsFields.ISSYNCEDTOWS]
        self.deleted=withings_tuple[self.WithingsFields.DELETED]
        self.deletionreason=withings_tuple[self.WithingsFields.DELETIONREASON]
        self.note=withings_tuple[self.WithingsFields.NOTE]
        self.snoringenabled=withings_tuple[self.WithingsFields.SNORINGENABLED]
        self.inprogress=withings_tuple[self.WithingsFields.INPROGRESS]
        self.manualstartdate=withings_tuple[self.WithingsFields.MANUALSTARTDATE]
        self.manualenddate=withings_tuple[self.WithingsFields.MANUALENDDATE]
        self.blankvasistasfilled=withings_tuple[self.WithingsFields.BLANKVASISTASFILLED]
        self.pathlists=withings_tuple[self.WithingsFields.PATHLISTS]
        self.cryptpart=withings_tuple[self.WithingsFields.CRYPTPART]
        self.coverpictureurl=withings_tuple[self.WithingsFields.COVERPICTUREURL]
        self.uris=withings_tuple[self.WithingsFields.URIS]
        self.coverpictureuri=withings_tuple[self.WithingsFields.COVERPICTUREURI]
        self.sleepscorevalue=withings_tuple[self.WithingsFields.SLEEPSCOREVALUE]
        self.sleepscorestatus=withings_tuple[self.WithingsFields.SLEEPSCORESTATUS]
        self.sleepscorealgoversion=withings_tuple[self.WithingsFields.SLEEPSCOREALGOVERSION]
        self.duration_info_score=withings_tuple[self.WithingsFields.DURATION_INFO_SCORE]
        self.duration_info_status=withings_tuple[self.WithingsFields.DURATION_INFO_STATUS]
        self.recovery_info_score=withings_tuple[self.WithingsFields.RECOVERY_INFO_SCORE]
        self.recovery_info_status=withings_tuple[self.WithingsFields.RECOVERY_INFO_STATUS]
        self.interruptions_info_score=withings_tuple[self.WithingsFields.INTERRUPTIONS_INFO_SCORE]
        self.interruptions_info_status=withings_tuple[self.WithingsFields.INTERRUPTIONS_INFO_STATUS]
        self.timetofallasleep_info_score=withings_tuple[self.WithingsFields.TIMETOFALLASLEEP_INFO_SCORE]
        self.timetofallasleep_info_status=withings_tuple[self.WithingsFields.TIMETOFALLASLEEP_INFO_STATUS]
        self.timetowakeup_info_score=withings_tuple[self.WithingsFields.TIMETOWAKEUP_INFO_SCORE]
        self.timetowakeup_info_status=withings_tuple[self.WithingsFields.TIMETOWAKEUP_INFO_STATUS]
        self.regularity_info_score=withings_tuple[self.WithingsFields.REGULARITY_INFO_SCORE]
        self.regularity_info_status=withings_tuple[self.WithingsFields.REGULARITY_INFO_STATUS]
        self.snoring_info_score=withings_tuple[self.WithingsFields.SNORING_INFO_SCORE]
        self.snoring_info_status=withings_tuple[self.WithingsFields.SNORING_INFO_STATUS]
        self.night_heartrate_info_score=withings_tuple[self.WithingsFields.NIGHT_HEARTRATE_INFO_SCORE]
        self.night_heartrate_info_status=withings_tuple[self.WithingsFields.NIGHT_HEARTRATE_INFO_STATUS]
        self.distance=withings_tuple[self.WithingsFields.DISTANCE]
        self.averagespeed=withings_tuple[self.WithingsFields.AVERAGESPEED]
        self.minspeed=withings_tuple[self.WithingsFields.MINSPEED]
        self.maxspeed=withings_tuple[self.WithingsFields.MAXSPEED]
        self.startlatitude=withings_tuple[self.WithingsFields.STARTLATITUDE]
        self.startlongitude=withings_tuple[self.WithingsFields.STARTLONGITUDE]
        self.endlatitude=withings_tuple[self.WithingsFields.ENDLATITUDE]
        self.endlongitude=withings_tuple[self.WithingsFields.ENDLONGITUDE]
        self.centerlatitude=withings_tuple[self.WithingsFields.CENTERLATITUDE]
        self.centerlongitude=withings_tuple[self.WithingsFields.CENTERLONGITUDE]
        self.spanlatitudedelta=withings_tuple[self.WithingsFields.SPANLATITUDEDELTA]
        self.spanlongitudedelta=withings_tuple[self.WithingsFields.SPANLONGITUDEDELTA]
        self.datajson_parsed = json.loads(self.datajson)
    counter = 0

    def __init__(self, withings_tuple):
        def to_timedelta(key):
            if key in self.datajson_parsed:
                return timedelta(seconds=(int(self.datajson_parsed[key])/1000))
            else:
                return timedelta(0)

        self.set_fields_from_tuple(withings_tuple)
        self.sleep = False

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

            # wake_up_duration      = to_timedelta("wakeUpDuration")
            # duration_to_sleep     = to_timedelta("durationToSleep")
            # duration_to_get_up    = to_timedelta("durationToGetUp")
            # wake_up_count         = self.datajson_parsed["wakeUpCount"]
            self.timedelta_in_bed = timedelta(seconds=(self.sleep_end-self.sleep_start))
            self.timedelta_slept = self.manual_sleep_duration + self.light_sleep_duration + self.deep_sleep_duration + self.rem_sleep_duration


        # typecat = "".join(list(self.datajson_parsed.keys()))

    def __str__(self):
        retstr = ""
        if self.sleep:
            retstr += "sleep ending on %s\n"%(time_util.epoch_to_yyyymmdd(self.enddate))
            retstr += "    sleep_start: %s\n"%time_util.prettify_epoch_time(self.sleep_start)
            retstr += "    sleep_end: %s\n"  %time_util.prettify_epoch_time(self.sleep_end)
            retstr += "    timedelta_in_bed: %s\n"%(self.timedelta_in_bed)
            retstr += "    timedelta_slept: %s\n"%self.timedelta_slept
        # retstr += "%s: %s\n"%("id",self.id)
        # retstr += "%s: %s\n"%("wsid",self.wsid)
        # retstr += "%s: %s\n"%("userid",self.userid)
        # retstr += "%s: %s\n"%("startdate",  time_util.prettify_epoch_time(self.startdate))
        # retstr += "%s: %s\n"%("enddate",    time_util.prettify_epoch_time(self.enddate))
        # retstr += "%s: %s\n"%("timezone",self.timezone)
        # retstr += "%s: %s\n"%("day",self.day)
        # retstr += "%s: %s\n"%("modifieddate",self.modifieddate)
        # retstr += "%s: %s\n"%("devicemodel",self.devicemodel)
        # retstr += "%s: %s\n"%("devicetype",self.devicetype)
        # retstr += "%s: %s\n"%("attrib",self.attrib)
        # retstr += "%s: %s\n"%("category",self.category)
        # retstr += "%s: %s\n"%("datajson",self.datajson)
        # retstr += "%s: %s\n"%("activityrecognitionversion",self.activityrecognitionversion)
        # retstr += "%s: %s\n"%("issyncedtows",self.issyncedtows)
        # retstr += "%s: %s\n"%("deleted",self.deleted)
        # retstr += "%s: %s\n"%("deletionreason",self.deletionreason)
        # retstr += "%s: %s\n"%("note",self.note)
        # retstr += "%s: %s\n"%("snoringenabled",self.snoringenabled)
        # retstr += "%s: %s\n"%("inprogress",self.inprogress)
        # retstr += "%s: %s\n"%("manualstartdate",time_util.prettify_epoch_time(self.manualstartdate))
        # retstr += "%s: %s\n"%("manualenddate",  time_util.prettify_epoch_time(self.manualenddate))
        # retstr += "%s: %s\n"%("blankvasistasfilled",self.blankvasistasfilled)
        # retstr += "%s: %s\n"%("pathlists",self.pathlists)
        # retstr += "%s: %s\n"%("cryptpart",self.cryptpart)
        # retstr += "%s: %s\n"%("coverpictureurl",self.coverpictureurl)
        # retstr += "%s: %s\n"%("uris",self.uris)
        # retstr += "%s: %s\n"%("coverpictureuri",self.coverpictureuri)
        # retstr += "%s: %s\n"%("sleepscorevalue",self.sleepscorevalue)
        # retstr += "%s: %s\n"%("sleepscorestatus",self.sleepscorestatus)
        # retstr += "%s: %s\n"%("sleepscorealgoversion",self.sleepscorealgoversion)
        # retstr += "%s: %s\n"%("duration_info_score",self.duration_info_score)
        # retstr += "%s: %s\n"%("duration_info_status",self.duration_info_status)
        # retstr += "%s: %s\n"%("recovery_info_score",self.recovery_info_score)
        # retstr += "%s: %s\n"%("recovery_info_status",self.recovery_info_status)
        # retstr += "%s: %s\n"%("interruptions_info_score",self.interruptions_info_score)
        # retstr += "%s: %s\n"%("interruptions_info_status",self.interruptions_info_status)
        # retstr += "%s: %s\n"%("timetofallasleep_info_score",self.timetofallasleep_info_score)
        # retstr += "%s: %s\n"%("timetofallasleep_info_status",self.timetofallasleep_info_status)
        # retstr += "%s: %s\n"%("timetowakeup_info_score",self.timetowakeup_info_score)
        # retstr += "%s: %s\n"%("timetowakeup_info_status",self.timetowakeup_info_status)
        # retstr += "%s: %s\n"%("regularity_info_score",self.regularity_info_score)
        # retstr += "%s: %s\n"%("regularity_info_status",self.regularity_info_status)
        # retstr += "%s: %s\n"%("snoring_info_score",self.snoring_info_score)
        # retstr += "%s: %s\n"%("snoring_info_status",self.snoring_info_status)
        # retstr += "%s: %s\n"%("night_heartrate_info_score",self.night_heartrate_info_score)
        # retstr += "%s: %s\n"%("night_heartrate_info_status",self.night_heartrate_info_status)
        # retstr += "%s: %s\n"%("distance",self.distance)
        # retstr += "%s: %s\n"%("averagespeed",self.averagespeed)
        # retstr += "%s: %s\n"%("minspeed",self.minspeed)
        # retstr += "%s: %s\n"%("maxspeed",self.maxspeed)
        # retstr += "%s: %s\n"%("startlatitude",self.startlatitude)
        # retstr += "%s: %s\n"%("startlongitude",self.startlongitude)
        # retstr += "%s: %s\n"%("endlatitude",self.endlatitude)
        # retstr += "%s: %s\n"%("endlongitude",self.endlongitude)
        # retstr += "%s: %s\n"%("centerlatitude",self.centerlatitude)
        # retstr += "%s: %s\n"%("centerlongitude",self.centerlongitude)
        # retstr += "%s: %s\n"%("spanlatitudedelta",self.spanlatitudedelta)
        # retstr += "%s: %s\n"%("spanlongitudedelta",self.spanlongitudedelta)
        # retstr += "%s: %s\n"%("datajson_parsed",self.datajson_parsed)
        return retstr.strip()


class WithingsTable(DBTable):
    def __init__(self):
        self.TABLE_NAME  = "WITHINGS_ENTRIES"
        fields = [\
            # Auction scan counter
            DBField("ID",     "INTEGER", True),
        ]
        parent=super(WithingsTable, self)
        parent.__init__(self.TABLE_NAME, fields)
