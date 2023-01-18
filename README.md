# Continuity-Mode-WIndows-Android-youtube-

This program uses windows clipboard synchronization to read the clipboard copied from the phone.
When you copy the link of a youtube video, it will automatically open on your PC.

Since the program checks the clipboard, and I don't know of any way to check which device some text was copied from, I implemented a function that checks if the link ends in ?t="number". by doing so, when you go to copy a link from the pc, if you check the box start from... the program will not run!

To enable clipboard synchronization look at the following link:
https://www.howtogeek.com/745838/how-to-sync-your-clipboard-between-windows-and-android/

Requirements:
-----------------------------------------------------------------------------
- Python 3.x
- pip install webbrowser  
- pip install time
- pip install infi.systray
- pip install re
- pip install pyperclip


How to Make the Program Run at Startup:
-----------------------------------------------------------------------------

1) Press Win+R and type shell:startup
![Screenshot (52)](https://user-images.githubusercontent.com/87772044/213161051-249d59e9-e073-4b9d-91a3-1a3a5215c0b2.png)

2) Create a Shortcup of the program
![Screenshot (50)](https://user-images.githubusercontent.com/87772044/213161161-2a83f071-9108-45bf-a36f-21d5ff6b5398.png)

3)Paste the shortcut inside the startup folder
![Screenshot (51)](https://user-images.githubusercontent.com/87772044/213161236-d44f3acd-4266-4c1d-a276-ec77ca92b006.png)


How to Close the program:
-----------------------------------------------------------------------------
you need to search for Python (Windowed) on task manager

![Screenshot (54)](https://user-images.githubusercontent.com/87772044/213166003-5bd7584a-4b13-4fd1-b7d6-4fb131df5d46.png)

