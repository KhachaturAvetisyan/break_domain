from json import load

# span_id = str(input())
# class_start_time = str(input())
# class_end_time = str(input())

span_id = "1"
class_start_time = "09:00:00"
class_end_time = "17:00:00"

class_start_time = list(map(lambda x: int(x), class_start_time.split(":")))
class_end_time = list(map(lambda x: int(x), class_end_time.split(":")))

f = open('data.json')
data = load(f)

print(class_start_time, class_end_time)
print(data[span_id])
