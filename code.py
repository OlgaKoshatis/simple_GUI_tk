from tkinter import *

root = Tk()

root.title('SpeedTest')
root.geometry('400x400')

button = Button(root, text='Click me', width=15, height=2, font=('Arial', 20), bg='MidnightBlue', fg='orangered')
button.pack(side=BOTTOM, pady=40)

download_label = Label(root, text='Скорость загрузки:\n-', font=('Arial', 20))
download_label.pack(side=TOP, pady=40)
upload_label = Label(root, text='Скорость отдачи:\n-', font=('Arial', 20))
upload_label.pack(side=TOP, pady=40)


root.mainloop()
