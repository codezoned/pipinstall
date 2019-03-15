#import module from script
import subprocess
import sys
import os
import argparse 
import platform

#Global Variables required

#os platform (windows, linus, etc)
system_platform = str.lower(platform.system())

#current working directory
path = os.getcwd()
if system_platform == 'windows':
	path = path + "\\" + 'domains' + "\\"
	print(path)
else:
	path = path + '/' + 'domains' + "/"
	print(path)

#Function definations:-

#Clear the terminal
def clear_screen():
	if system_platform =='windows':
		os.system('cls')
	else:
		os.system('clear')

#check for command line arguments
def check_args(args = None):
	if args == None:
		print("Please enter the required arguments!")

	parser = argparse.ArgumentParser(description= "pipinstall: a library to download multiple libraries in different domains at once.")
	parser.add_argument("domain_name", 
		help= "Domain name",
		type = str)

	return parser.parse_args(args)

#run the script
def Main():

	clear_screen()
	print('Welcome to pipinstall')

	if check_args(sys.argv[1:]).domain_name:
		required_domain = check_args(sys.argv[1:]).domain_name

		global path, system_platform
		if system_platform == 'windows':
			backslash = '\ '
			backslash = backslash.strip(backslash)
			path = path + backslash + required_domain + backslash

			try:
				os.chdir(path)

				#run the command :- install all packages in requirements.txt
				#-U specifies upgrade packages if a package is already installed	
				subprocess.call([sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"])
			except OSError:
				print('No domain found. Please try again.')
			
		else:
			path = path + '/' + required_domain + '/'
			
			try:
				os.chdir(path)

				#run the command :- install all packages in requirements.txt
				#-U specifies upgrade packages if a package is already installed	
				subprocess.call([sys.executable, "-m", "pip", "install", "-U", "-r", "requirements.txt"])
			except OSError:
				print('No domain found. Please try again.')

		# #to check for files in cwd	
		# print(path)
		# files = [f for f in os.listdir('.') if os.path.isfile(f)]
		# for f in files:
		# 	print(f + "\n")

if __name__ == '__main__':
	Main()
	# os.system('setx /M path "%path%;"+path')