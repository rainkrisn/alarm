from tkinter import *
from playsound import playsound
from PIL import Image, ImageTk

root = Tk()

def time():
    time_in_mins = dropdown.get()
    print(time_in_mins)

def ringtone():
    playsound(r'c:\Users\aniru\Downloads\Nokia ringtone arabic.mp3')


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

label = Label(root, text = "Enter the time: ", font = ("Consolas", 10, 'bold'))
label.place(x=30, y=100)

dropdown = Scale(root, from_=0,to=60)
dropdown.place(x=150, y=50)

button = Button(root, text="Submit", font = ("Consolas", 20, 'italic'))
button.config(command = time)
button.place(x=200, y=50)

root.mainloop()
