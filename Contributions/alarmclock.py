import tkinter as t
from datetime import datetime
import time
import winsound
# -------------------------------FUNCTION---------------------------------------------



def clock():
    hour = int(hour_entry.get())
    second = int(sec_entry.get())
    mintue = int(min_entry.get())

    print(f"{(hour > 24 and second > 60) and mintue > 60}")
    LETSG0 = True

    if (hour > 24 or second > 60) or mintue > 60:
        heading_label.config(text = 'please put valid time', bg ='red')
    else:
        if second == 0:
            second = '00'

        wakeup = f"{hour}:{mintue}:{second}"
        while(LETSG0):

            now = datetime.now()
            date_time = now.strftime('%H:%M:%S')
            print(date_time)
            print(wakeup)
            time.sleep(1)
            if date_time == wakeup:
                LETSG0 = False
                winsound.PlaySound('sound.wav',winsound.SND_ASYNC)





# --------------GUI--------------------------------------

box = t.Tk()
box.title("ALARAM CLOCK")
box.geometry('700x200')

heading_label = t.Label(text= 'Enter time in 24 hour format',font = ('Arial',10), bg = '#F3FEB0')
heading_label.grid(row = 0,column = 1, columnspan = 2,pady = 10)

hour_label = t.Label(text = 'hour',font = ('Arial',10))
hour_label.grid(row = 1,column = 1,padx = 10,pady = 10 )
hour_entry = t.Entry(bg = '#FC4B50')
hour_entry.grid(row = 2, column = 1, padx = 10)

min_label = t.Label(text = 'min', font = ('Arial',10))
min_label.grid(row = 1 , column = 2, padx = 10)
min_entry = t.Entry(bg = '#FC4B50')
min_entry.grid(row = 2, column = 2, padx = 10)

sec_label = t.Label(text = 'Sec', font = ('Arial',10))
sec_label.grid(row = 1 , column = 3,padx = 10)
sec_entry = t.Entry(bg = '#FC4B50')
sec_entry.grid(row = 2, column = 3, padx = 10)

time_label = t.Label(text = 'When do you want to wake up',font=('Arial',10),bg = 'blue')
time_label.grid(row = 2, column = 0)

setalaram = t.Button(text = 'Setupalalaram', command = clock, bg = '#B3E0F2')
setalaram.grid(row = 3, column = 1,columnspan = 2, pady = 30)

box.mainloop()
