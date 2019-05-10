# import module from script
import sys
import os
import subprocess
#from pathlib import Path

# Function definations:-

# Clear the terminal
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# end of clear_screen

#install_dom function
def install_dom(dpath):
    os.chdir(dpath)
    os.getcwd()
    #subprocess call to install libraries
    subprocess.call([sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"])
#End of install_dom 