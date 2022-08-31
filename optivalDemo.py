from datetime import datetime

dt_string = datetime.now()
current_time= dt_string.strftime("%d/%m/%Y %H:%M:%S")

print(current_time)