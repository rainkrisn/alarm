from tkinter import *
from playsound import playsound

root = Tk()

root.title("Alarm Clock - Made by Rain")
root.geometry("400x500")

alarm_welcome = Label(root, text = "Alarm Clock", font = ("Consolas", 15, "bold"))
alarm_welcome.pack()

byline = Label(root, text="Made by Rain", font = ("Consalas", 10, 'italic'))
byline.place(x=150, y=30)


# playsound(r'c:\Users\aniru\Downloads\Nokia ringtone arabic.mp3')

root.mainloop()
