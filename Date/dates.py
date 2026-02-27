import datetime as dt
time1 = dt.datetime.now()
time2 = time1.strftime("%A")
time3 = time1.strftime("%a")
time4 = time1.strftime("%b")
time5 = time1.strftime("%B")
print(time1, time2, time3, time4, time5)
