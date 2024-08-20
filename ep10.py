from datetime import datetime

dt_string = "2024-06-20 11:00:00"
dt_object = datetime.strptime(dt_string, '%Y-%m-%d %H:%M:%S')
epoch = int(dt_object.timestamp())
print(epoch)