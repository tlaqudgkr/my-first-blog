from datetime import datetime
import pytz

def makeDate(y,m,d):
    dt = datetime(y,m,d,tzinfo=pytz.utc)
    return dt

def makeDateTime(y,m,d,h,n,s):
    dt = datetime(y,m,d,h,n,s,tzinfo=pytz.utc)
    return dt