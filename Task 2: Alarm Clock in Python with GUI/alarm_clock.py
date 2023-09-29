# Import the tkinter.ttk module for themed widgets.
from tkinter.ttk import *

# Import the tkinter module for basic GUI widgets.
from tkinter import *

# Import the PIL.ImageTk and PIL.Image modules for image support.
from PIL import ImageTk, Image

# Import the datetime module for date and time handling.
from datetime import datetime

# Import the time module for sleep() functionality.
from time import sleep

# Import the pygame.mixer module for audio playback.
from pygame import mixer

# Import the threading module for multi-threading.
from threading import Thread

# Import the start_alarm() and stop_alarm() functions from the alarm_methods module.
from alarm_methods import stop_alarm



# Create a Tkinter window
window = Tk()

# Set the title of the window to "Clock"
window.title("Clock")

# Set the size of the window to 400x160 pixels
window.geometry("400x160")

# Set the background color of the window to #FFE9C2 (light peach)
window.configure(bg="#FFE9C2")
  

# Create a frame with a width of 402 pixels and a height of 6 pixels, with a background color of #00F7F3.
frame_line = Frame(window, width=402, height=6, bg="#00F7F3")

# Place the frame in the 0th row and 0th column of the grid.
frame_line.grid(row=0, column=0)


# Create a frame with a width of 402 and a height of 291, with a light purple background color.
frame_body = Frame(window, width=402, height=291, bg="#FFABF1")

# Place the frame on the grid in row 1, column 0.
frame_body.grid(row=1, column=0)


# Open the image file "alarm.png"
img = Image.open('alarm.png')

# Resize the image to a width of 110 pixels and a height of 110 pixels, using the ANTIALIAS filter to produce a smooth image
img = img.resize((110, 110), Image.ANTIALIAS)

# Convert the PIL Image object to a Tkinter PhotoImage object
img = ImageTk.PhotoImage(img)


# Create a Label widget to display the application logo.
app_image = Label(frame_body, height=105, image=img, bg="#FFABF1")

# Place the Label widget at the top left corner of the frame.
app_image.place(x=11, y=11)


# Create a Label widget with the text "Alarm", a height of 2, an Arial font, and a light pink background color
name = Label(frame_body, text="Alarm", height=2, font=("Arial"), bg="#FFABF1")

# Place the Label widget at coordinates (140, 11) in the frame
name.place(x=140, y=11)


# Create a Label widget to display the text "Hours"
hour = Label(frame_body, text = "Hours", height=2, font=("Arial"), bg="#FFABF1")

# Place the Label widget at position (140, 41) in the frame_body widget
hour.place(x=140, y=41)

hrs = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# Create a Combobox object to select the current hour
c_hour = Combobox(frame_body, width=3, font=("Arial", 14), values=[h for h in hrs])

# Set the default value of the Combobox to the first hour in the list
c_hour.current(0)

# Place the Combobox at the coordinates (140, 80)
c_hour.place(x=140, y=80)

mins = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34','35', '36', '37', '38', '39', '40',
        '41', '42', '43', '44','45', '46', '47', '48', '49', '50', '51', '52', '53', '54','55', '56', '57', '58', '59', '60']

# Create a Label widget with the text "Mins", height 2, Arial font, and background color #FFABF1.
minutes = Label(frame_body, text = "Mins", height=2, font=("Arial"), bg="#FFABF1")

# Place the Label widget at coordinates (200, 41).
minutes.place(x=200, y=41)



# Create a Combobox widget with 3 characters width, Arial 14 font, and values from the `time_elements.mins` list.
c_min = Combobox(frame_body, width=3, font=("Arial", 14), values=[m for m in mins])

# Set the current selection of the Combobox widget to the first item.
c_min.current(0)

# Place the Combobox widget at coordinates (200, 80).
c_min.place(x=200, y=80)

secs = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30','31', '32', '33', '34','35', '36', '37', '38', '39', '40',
        '41', '42', '43', '44','45', '46', '47', '48', '49', '50', '51', '52', '53', '54','55', '56', '57', '58', '59', '60']

# Create a Label widget with the text "Secs", height 2, Arial font, and background color #FFABF1.
seconds = Label(frame_body, text="Secs", height=2, font=("Arial"), bg="#FFABF1")

# Place the Label widget at coordinates (260, 41).
seconds.place(x=260, y=41)



# Create a Combobox widget to select the seconds
c_secs = Combobox(frame_body, width=3, font=("Arial", 14), values=[s for s in secs])

# Set the default value to the first second
c_secs.current(0)

# Place the Combobox widget at position (260, 80)
c_secs.place(x=260, y=80)


# Create a Label widget with the text "Period", height 2, Arial font, and background color #FFABF1.
period = Label(frame_body, text="Period", height=2, font=("Arial"), bg="#FFABF1")

# Place the Label widget at coordinates (320, 41).
period.place(x=320, y=41)

# Create a Combobox widget for the customer period, with a width of 3, font of Arial 14, and values of AM and PM.
c_period = Combobox(frame_body, width=3, font=("Arial", 14), values=["AM", "PM"])

# Set the current value of the Combobox widget to AM.
c_period.current(0)

# Place the Combobox widget at coordinates (320, 80) in the frame.
c_period.place(x=320, y=80)

def start_alarm():
    t = Thread(target=alarm)
    t.start()

    
# Create an integer variable to store the selected value
selected = IntVar()


# Create a radio button with the text "Start", value 1, variable `selected`, font "Arial", background color "#FFABF1", and command `start_alarm`.
radio1 = Radiobutton(frame_body, text='Start', value=1, variable=selected, font=("Arial"), bg="#FFABF1", command=start_alarm)

# Place the radio button at coordinates (140, 120).
radio1.place(x=140, y=120)



def sound_alarm():
    
    """Plays the magic system sound effect and resets the selected option to 0."""
    
    # Load the magic system sound effect
    mixer.music.load('magic_system.mp3')
    
    # Play the magic system sound effect
    mixer.music.play()
    
    # Reset the selected option to 0
    selected.set(0)



    # Create a Radiobutton object with the text "Stop", value 1, variable selected, Arial font, background color #FFABF1, and command stop_alarm.
    radio2 = Radiobutton(frame_body, text='Stop', value=2, variable=selected, font=("Arial"), bg="#FFABF1", command=stop_alarm)

    # Place the Radiobutton object at coordinates (200, 120).
    radio2.place(x=200, y=120)


    
def alarm():
    """
    This function defines an alarm clock.

    Args:
        None

    Returns:
        None
    """

    while True:
        """
        This loop keeps the alarm clock running.
        """
        # This line gets the hour from the alarm clock.
        alarm_hour = c_hour.get()
        
        # This line gets the minutes from the alarm clock.
        alarm_minutes = c_min.get()
        
        # This line gets the seconds from the alarm clock.
        alarm_secs = c_secs.get()
        
        # This line gets the period from the alarm clock. 
        alarm_period = c_period.get()
        
        
        
  
        
        # Get the current date and time
        now = datetime.now()
        
        # Get the current hour, minute, second, and period.
        
        # %I is the 12-hour format of the hour, without leading zeros.
        hour = now.strftime("%I")  
        
        # %M is the minute, with leading zeros.
        minute = now.strftime("%M")  
        
        # %S is the second, with leading zeros.
        second = now.strftime("%S")  
        
        # %p is the AM/PM period.
        period = now.strftime("%p")  

        # Print the system clock to the console.
        print('system clock:', ' ', hour, minute, second, period)
        
        # Add a blank line.
        print(' ')

        
        
        # Check if the alarm time has been reached.
        if alarm_period == period:
            
            # Check if the alarm hour has been reached.
            if alarm_hour == hour:
                
                # Check if the alarm minute has been reached.
                if alarm_minutes == minute:
                    
                    # Check if the alarm second has been reached.
                    if alarm_secs == second:
                        
                        # Print the alarm time and the wake-up message.
                        print('user_set_alarm: ',alarm_hour, alarm_minutes, alarm_secs, alarm_period)
                        print(' ')
                        print("WAKE UP! LET'S GET GOING.")
                        
                        # Play the alarm sound.
                        sound_alarm()
                        
                        # Break out of the loop.
                        break
                    
        # Sleep for 1 second.
        sleep(1)

       
# Initialize the Pygame mixer.
mixer.init()

# Start the Tkinter mainloop.
window.mainloop()
