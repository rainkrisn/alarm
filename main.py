from tkinter import *
#from tkinter.ttk import *
from tkinter import colorchooser
import time 
from playsound import playsound
from PIL import Image, ImageTk
from colorsys import rgb_to_hls, hls_to_rgb

root = Tk()

root.title("Alarm Clock - Made by Rain") # geometry for the window
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
byline = Label(root, text="Made by Rain", font=("Consolas", 10, 'italic'),)
byline.place(x=150, y=25)

def get_complementary_color(hex_color):
    try:
        # Remove the '#' if present
        hex_color = hex_color.lstrip('#')
        
        
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) # calculating rgb values
        
        
        h, l, s = rgb_to_hls(rgb[0]/255.0, rgb[1]/255.0, rgb[2]/255.0)
        
        
        comp_h = (h + 0.5) % 1.0
        
        
        comp_rgb = hls_to_rgb(comp_h, l, s)
        
        
        comp_rgb = tuple(max(0, min(int(x * 255), 255)) for x in comp_rgb)
        
        
        return '#{:02x}{:02x}{:02x}'.format(*comp_rgb)
    except Exception as e:
        print(f"Error in get_complementary_color: {e}")
        return "#000000"  

def colour():
    global dropdown, button, submit_button  # Ensure these are accessible

    colour = colorchooser.askcolor()
    if not colour[1]:  # User cancelled the color chooser
        return
    
    colourHex = colour[1]
    
    try:
        # Calculate complementary color
        comp_color = get_complementary_color(colourHex)
        
        # Update all widgets
        for widget in root.winfo_children():
            if isinstance(widget, (Button, Label, Scale)):
                widget.config(fg=comp_color, bg=colourHex)
            
            # Special handling for Scale widget
            if isinstance(widget, Scale):
                widget.config(troughcolor=colourHex, activebackground=comp_color)

        # Update the root window background
        root.config(bg=colourHex)
    except Exception as e:
        print(f"Error in colour function: {e}")

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

#progress = Progressbar(root, orient=HORIZONTAL, length=100)
#progress.pack()

label = Label(root, text = "Enter the time: ", font = ("Consolas", 10, 'bold')) 
label.place(x=30, y=100)

dropdown = Scale(root, from_=0,to=60)
dropdown.place(x=150, y=50)

submit_button = Button(root, text="Submit", font=("Consolas", 20, 'italic'), command=time)
submit_button.place(x=200, y=50)

button = Button(root, text="Choose Colour", font=("Consolas", 8, 'bold'), command=colour)
button.place(x=150, y=450)

root.mainloop()
