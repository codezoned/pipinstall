# import module from script
import sys
import os
import subprocess
import argparse
import platform


# locate the project folder
# path will be used as global
pathname = os.path.dirname(sys.argv[0])
abs_path = os.path.abspath(pathname)
path = os.path.join(os.path.normpath(abs_path), 'domains')


# Function definations:-

# Clear the terminal
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
# end of clear_screen


# check for command line arguments
def check_args(args=None):
    if args == None:
        print("Please enter the required arguments!")

    parser = argparse.ArgumentParser(
        description="pipinstall: a library to download multiple libraries in different domains at once.")
    parser.add_argument("domain_name",
                        help="Domain name",
                        type=str)

    return parser.parse_args(args)
# end of check_args


# Main function
def Main():

    clear_screen()
    print("Welcome to pipinstall! A humble try to make our lives easier :')")

    if check_args(sys.argv[1:]).domain_name:
        required_domain = check_args(sys.argv[1:]).domain_name

        global path
        path = os.path.join(path, required_domain)
        print(path)
        os.chdir(path)
        print(os.getcwd())

        subprocess.call([sys.executable, "-m", "pip",
                         "install", "-U", "-r", "requirements.txt"])


# call Main
if __name__ == '__main__':
    Main()
