import subprocess
import sys

libraries = ["pygetwindow","tkinter","time","keyboard","pyautogui"]

for library in libraries:
    try:
        __import__(library)
        print(f"'{library}' is already installed.")
    except ImportError:
        print(f"'{library}' not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])
