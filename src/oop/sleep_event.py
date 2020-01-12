import sys
from datetime import datetime, timedelta
sys.path.insert(0, "../utils")

import time_util

class SleepEvent():
    def __init__(self, sleep_start, sleep_end, timedelta_slept=None):
        self.sleep_start = sleep_start
        self.sleep_end = sleep_end
        self.timedelta_slept = timedelta_slept
        self.sleep_opportunity = self.sleep_end - self.sleep_start

    def __str__(self):
        sleep_opportunity_hr_str = "%5s" % ("%2.2f"%(self.sleep_opportunity/60/60))

        # populate sleep opportunity field if it's been set
        sleep_opportunity_print_str = ""
        if self.timedelta_slept:
            timedelta_slept_hr_str     = "%5s" % ("%2.2f"%(self.timedelta_slept.seconds/60/60))
            sleep_opportunity_print_str = " hours out of %s sleep opportunity." % sleep_opportunity_hr_str

        retstr = ""
        retstr += "%s -- %s: slept %s%s" % (\
                                        time_util.epoch_to_md_hm(self.sleep_start),\
                                        time_util.epoch_to_md_hm(self.sleep_end),\
                                        timedelta_slept_hr_str,\
                                        sleep_opportunity_print_str)
        return retstr

    def to_db_tuple(self):
        return (time_util.epoch_to_yyyymmdd(self.sleep_end), self.sleep_start, self.sleep_end, self.timedelta_slept.seconds)
