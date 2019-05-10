import os
import sys
import argparse
import utils

#Functions
#Path to domains folder
def domainPath():

    abs_path = os.path.abspath(__file__)
    fileDir = os.path.dirname(abs_path)
    path = os.path.join(fileDir, 'Domains')
    print(path)
    return path
#end of domainPath

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

    utils.clear_screen()
    print("Welcome to pipinstall! A humble try to make our lives easier :')")

    if check_args(sys.argv[1:]).domain_name:
        required_domain = check_args(sys.argv[1:]).domain_name

        dpath = domainPath()
        dpath = os.path.join(dpath, required_domain)
        if os.path.isdir(dpath):
            utils.install_dom(dpath)
        else:
            while not os.path.isdir(dpath):
                domain_name = str(input('Domain Name does not exist.\nPlease re-enter the domain name:'))
                dpath = os.path.join(dpath, domain_name)
                if os.path.isdir(dpath):
                    utils.install_dom(dpath)


# call Main
if __name__ == '__main__':
    Main()

