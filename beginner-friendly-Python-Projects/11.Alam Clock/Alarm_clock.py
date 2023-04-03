import time
from playsound import playsound
from tkinter import Tk, Label, Button, Entry

def set_alarm():
    alarm_time = entry.get()
    alarm_hour = alarm_time.split(':')[0]
    alarm_minute = alarm_time.split(':')[1]

    while True:
        current_time = time.localtime()
        current_hour = time.strftime("%H", current_time)
        current_minute = time.strftime("%M", current_time)

        if (current_hour == alarm_hour) and (current_minute == alarm_minute):
            playsound('alarm_sound.mp3')
            break

def main():
    global entry
    window = Tk()
    window.geometry('300x200')
    window.title('Alarm Clock')

    title = Label(text='Enter time (HH:MM)')
    title.pack(pady=10)

    entry = Entry(window)
    entry.pack(pady=10)

    button = Button(text='Set Alarm', command=set_alarm)
    button.pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    main()
