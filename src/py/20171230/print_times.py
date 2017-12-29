import datetime
import pytz

aware_now = datetime.datetime.now(pytz.UTC)
zones = pytz.common_timezones
awares = []

for s in zones:
    zone = pytz.timezone(s)
    aware = aware_now.astimezone(zone)
    aware = aware.replace(microsecond=0)
    awares.append(aware)

ss = []

for aware in awares:
    ss.append(aware.isoformat())

naives = []

for aware in awares:
    naives.append(aware.replace(tzinfo=None))

lis = zip(zones, awares, ss, naives)
lis = sorted(lis, key=lambda x: x[0])
lis = sorted(lis, key=lambda x: x[3])
len_zone = max(len(x) for x in zones)
len_s = max(len(x) for x in ss)

for zone, aware, s, naive in lis:
    print("{: <{}} {: >{}}".format(zone, len_zone, s, len_s))
