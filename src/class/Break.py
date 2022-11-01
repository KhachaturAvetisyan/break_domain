from _datetime import datetime, timedelta

class_start_time = '09:00:00'
class_end_time = '17:00:00'



st = "01:30:00"

time_dict = {'00' : 0,
             '01' : 1,
             '02' : 2,
             '03' : 3,
             '04' : 4,
             '05' : 5,
             '06' : 6,
             '07' : 7,
             '08' : 8,
             '09' : 9,
             '10' : 10,
             '11' : 11,
             '12' : 12,
             '13' : 13,
             '14' : 14,
             '15' : 15,
             '16' : 16,
             '17' : 17,
             '18' : 18,
             '19' : 19,
             '20' : 20,
             '21' : 21,
             '22' : 22,
             '23' : 23,
             '24' : 24,
             '25' : 25,
             '26' : 26,
             '27' : 27,
             '28' : 28,
             '29' : 29,
             '30' : 30}

start = datetime.strptime(class_start_time, '%H:%M:%S')
result = start + timedelta(hours=time_dict[st[:2]], minutes=time_dict[st[3:5]], seconds=time_dict[st[6:]])
print(type(result.time()))