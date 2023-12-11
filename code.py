from tkinter import *
from speedtest import Speedtest

def test():
    download = Speedtest().download()
    upload = Speedtest.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Скорость загрузки:\n" + str(download_speed) + "MbPs")
    upload_label.config(text="Скорость отдачи:\n" + str(upload_speed) + "MbPs")

root = Tk()

root.title('SpeedTest')
root.geometry('400x400')

button = Button(root, text='Click me', width=15, height=2, font=('Arial', 20), bg='MidnightBlue', fg='orangered')
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text='Скорость загрузки:\n-', font=('Arial', 20))
download_label.pack(side=TOP, pady=(50, 0))
upload_label = Label(root, text='Скорость отдачи:\n-', font=('Arial', 20))
upload_label.pack(side=TOP, pady=(10, 0))


root.mainloop()
