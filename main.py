import pygetwindow as gw
from tkinter import messagebox
import time
import keyboard
import pyautogui

print("If the Discord window doesn't open and you get an error, open it manually.")
id=input("Enter username to spam :")

def switch_tab(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if windows:
        windows[0].restore()
        time.sleep(5)
        windows[0].activate()
        return True
    
    else:
        return False

if switch_tab("Discord"):
    if id[0]=="@" :
        while True:
            if keyboard.is_pressed("esc"):
                messagebox.showinfo("Info","Thanks for using.")
                exit()
            
            else :
                pyautogui.write(id)
                keyboard.press_and_release("enter")
                keyboard.press_and_release("enter")
                time.sleep(0.5)

    else :
        while True:
            if keyboard.is_pressed("esc"):
                messagebox.showinfo("Info","Thanks for using.")
                exit()
            
            else :
                pyautogui.write(f"@{id}")
                keyboard.press_and_release("enter")
                keyboard.press_and_release("enter")
                time.sleep(0.5)

else :
    messagebox.showerror("Error","There was an error finding your Discord window.")
