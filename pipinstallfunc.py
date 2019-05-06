import sys
import os
import subprocess
import argparse

#Functions

#Path to domains folder
def domainPath():

    abs_path = os.path.abspath(__file__)
    fileDir = os.path.dirname(abs_path)
    path = os.path.join(fileDir, 'Domains')
    print(path)
    return path
#end of domainPath

def install_domain(domain_name = None):
    if domain_name = None:
        print("Please enter a valid domain name")
    path = domainPath()
    #going to the folder of the domain
    path = os.path.join(path, domain_name)
    os.chdir(path)
    subprocess.call([sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"])
    
instal_domain('cryptography')

