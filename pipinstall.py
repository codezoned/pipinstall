import os
import sys
import argparse
import subprocess

#Functions

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

#Path to domains folder
def domainPath():
    abs_path = os.path.abspath(__file__)
    fileDir = os.path.dirname(abs_path)
    path = os.path.join(fileDir, 'Domains')
    print(path)
    return path
#end of domainPath

#install function
def install(domain_name=None):
    #clear_screen()
    print("Welcome to pipinstall! A humble try to make our lives easier :D")

    if domain_name is not None:
        dpath = domainPath()
        dpath = os.path.join(dpath, domain_name)

        if os.path.isdir(dpath):
            install_dom(dpath)
        else:
            while not os.path.isdir(dpath):
                domain_name = str(input("Domain name does not exist. Please enter a valid domain name:\n"))
                dpath = os.path.join(dpath,domain_name)
                if os.path.isdir(dpath):
                    install_dom(dpath)

