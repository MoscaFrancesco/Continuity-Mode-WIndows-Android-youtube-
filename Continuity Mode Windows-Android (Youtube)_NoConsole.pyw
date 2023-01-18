import pyperclip
import webbrowser
import time
import re
import pystray
from pystray import MenuItem as item

# ------------------------------ Copied From Pc? ----------------------------- #
#This function checks if the copied string was copied from the pc or from the phone, the only way to do this is to check if it ends in ?t="number"
# , this implies that when you copy a youtube link from the pc , you have to check the option start from...
# t= stands for time=hours:minutes:seconds (107 = 1min, 7s)

def check_numbers(string):
    parts = string.split("?t=")
    if len(parts)>1:
        match = re.search(r'^\d+$', parts[1])
        if match:
            return True
    return False


global clipboard
clipboard =""

#first startup?
global start
start=0

while True:

    #current and previous clipboard
    clipboard_Old=clipboard
    clipboard = pyperclip.paste()

    #Checking whether the text has been copied from the PC    global fromPC
    fromPC = False
    if clipboard != clipboard_Old and start!=0:
        fromPC = check_numbers(clipboard)

    #Don't check the clipboard on first startup ---> start != 0
    #If I copy a new text from phone , then I run
    if clipboard != clipboard_Old and start!=0 and not fromPC == True:
        print(clipboard)
        if clipboard.startswith("https://youtu.be/"):
            print("Opening Youtube")
            webbrowser.open(clipboard)

    elif fromPC == True:
        print("the link is copied from pc")
        fromPc = False

    start = 1
    time.sleep(1)

