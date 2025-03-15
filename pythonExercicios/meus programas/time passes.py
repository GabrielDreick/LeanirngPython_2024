from datetime import datetime

def time_now():
    return datetime.today().time().second


time_mark = datetime.today().time().second
print(time_mark)
c = str(input("up or down?"))
if time_mark + 2 < time_now():
    print('too late')
else:
    print(c)