#How to Convert datetime to date without seconds
from datetime import datetime
dt = datetime.strptime('2016-06-01 16:05:20', '%Y-%m-%d %H:%M:%S').date()
print(dt)