from pylab import *
import os
from collections import namedtuple

_ntuple_diskusage = namedtuple('usage', 'total used free')

def disk_usage(path):
    """Return disk usage statistics about the given path.

    Returned valus is a named tuple with attributes 'total', 'used' and
    'free', which are the amount of total, used and free space, in bytes.
    """
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    return _ntuple_diskusage(total, used, free)

res = disk_usage('/')
used = (float(res.used) / float(res.total)) * 100
free = (float(res.free) / float(res.total))*100
# make a square figure and axes
fig = figure(1, figsize=(6,6))
fig.canvas.set_window_title('ResMan')
ax = axes([0.1, 0.1, 0.8, 0.8])

# The slices will be ordered and plotted counter-clockwise.
lblFree = 'Free: ' + str(round(float(res.free) / 10.0**9, 3)) + ' GB'
lblUsed = 'Used: ' + str(round(float(res.used) / 10.0**9, 3)) + ' GB'
labels = [lblFree, lblUsed]
fracs = [free, used]
explode=(0, 0)

pie(fracs, labels=labels, autopct='%1.1f%%', colors=['g', 'r'], shadow=True)
title('Available Hard Drive Space', bbox={'facecolor':'0.8', 'pad':5})
show()
