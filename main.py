from tkinter import *
import time 
from playsound import playsound
from PIL import Image, ImageTk

root = Tk()

root.title("Alarm Clock - Made by Rain")
root.geometry("400x500")

# load the image
image_path = r'c:\Users\aniru\Downloads\alarm clock.png'
img_open = Image.open(image_path)
img_resized = img_open.resize((25, 25))  
img = ImageTk.PhotoImage(img_resized)

# create a Label with both text and image
alarm_welcome = Label(root, text="Alarm Clock", font=("Consolas", 15, "bold"), compound=LEFT, image=img)
alarm_welcome.pack()

# author name etc
byline = Label(root, text="Made by Rain", font=("Consolas", 10, 'italic'))
byline.place(x=150, y=25)

def countdown(time_in_mins):
    time_left = time_in_mins * 60  # Convert minutes to seconds
    countdown_label = Label(root, font=("Consolas", 20, "bold"))
    countdown_label.place(x=150, y=200)

    def update_countdown():
        nonlocal time_left
        if time_left > 0:
            mins, secs = divmod(time_left, 60)
            time_string = f"{mins:02d}:{secs:02d}"
            countdown_label.config(text=time_string)
            time_left -= 1
            root.after(1000, update_countdown)
        else:
            countdown_label.config(text="Time's up!")
            ringtone()

    update_countdown()

def time():
    time_in_mins = dropdown.get()
    if time_in_mins == 0:
        label = Label(root, text="Please enter a value above 0!", font=("Consolas", 10, 'bold'))
        label.place(x=75, y=200)
    else:
        label = Label(root, text=f"Alarm set for {time_in_mins} minute{'s' if time_in_mins > 1 else ''}")
        label.pack()
        countdown(time_in_mins)

def ringtone():
    playsound(r'c:\Users\aniru\Downloads\Nokia ringtone arabic.mp3')

label = Label(root, text = "Enter the time: ", font = ("Consolas", 10, 'bold'))
label.place(x=30, y=100)

dropdown = Scale(root, from_=0,to=60)
dropdown.place(x=150, y=50)

button = Button(root, text="Submit", font=("Consolas", 20, 'italic'), command=time)
button.place(x=200, y=50)

root.mainloop()
