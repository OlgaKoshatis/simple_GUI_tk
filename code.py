from tkinter import *
from speedtest import Speedtest


def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)

    download_label.config(text="Скорость загрузки:\n" + str(download_speed) + 'Mbit/s')
    upload_label.config(text="Скорость отдачи:\n" + str(upload_speed) + "Mbit/s")


root = Tk()

root.title('SpeedTest')
root.geometry('300x400')

button = Button(root, text='Click me', width=15, height=2, font=('Arial', 20), borderwidth=5, relief=GROOVE)
button.pack(side=BOTTOM, pady=40, bg='SteelBlue', fg='Silver')

download_label = Label(root, text='Скорость загрузки:\n-', font=('Arial', 20))
download_label.pack(side=TOP, pady=(50, 0), bg='SteelBlue', fg='Silver')
upload_label = Label(root, text='Скорость отдачи:\n-', font=('Arial', 20))
upload_label.pack(side=TOP, pady=(10, 0))


root.mainloop()
