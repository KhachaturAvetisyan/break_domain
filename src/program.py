from json import load
from _datetime import datetime, timedelta

# span_id = str(input())
# class_start_time = str(input())
# class_end_time = str(input())

span_id = "1"
class_start_time = "09:00:00"
class_end_time = "17:00:00"

class_start_time = datetime.strptime(class_start_time, '%H:%M:%S')
class_end_time = datetime.strptime(class_end_time, '%H:%M:%S')

# class_start_time = list(map(lambda x: int(x), class_start_time.split(":")))
# class_end_time = list(map(lambda x: int(x), class_end_time.split(":")))

f = open('data.json')
data = load(f)

# print(class_start_time)
# print(class_end_time)
# print(class_end_time - class_start_time)

# print(data[span_id])

duration = {}

for el in data[span_id]:

    duration[el['id']] = list()

    if el['start_time_type'] == 'RELATIVE_TO_CLASS_START':
        for time in el['start_times']:
            t = datetime.strptime(time, '%H:%M:%S')
            delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            duration[el['id']].append((class_start_time + delta).time())

    if el['start_time_type'] == 'RELATIVE_TO_SHIFT_END':
        for time in el['start_times']:
            t = datetime.strptime(time, '%H:%M:%S')
            delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
            duration[el['id']].append((class_start_time - delta).time())

print(duration)