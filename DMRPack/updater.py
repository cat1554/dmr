#Set to True if need debug messages
ENABLE_DEBUG = False

import os
import time
import sys
import wget

version = None

print("DMR Pack Updater Script")

packDir = input(f"Please input Texture Pack Directory Path (Current : {os.getcwd()}) > ") #obtain directory path

os.chdir(packDir) # change dir to pack directory 

#for debugging purposes
if ENABLE_DEBUG: #look at line 2
    print(os.getcwd())

    print(os.listdir())


# obtain version file into . version . variable
try:
    versionfile = open("version","r")
    version = versionfile.read()
except FileNotFoundError: # except incorrect file 
    print("FATAL : Could not find version File. Please check Pack Directory\nTerminating in 15 Seconds")
    time.sleep(15)
    sys.exit(0)
    
print(f"Current Version Is : {version}") # print current 

latest = None

obtainlatest = input("Obtain Latest Version Info \n(Will Download Temporary File named \"latest\" IF THIS FILE ALEREADY EXISTS IT WILL GET CORRUPTED) \n(Y / N) > ")
if obtainlatest == "y" or obtainlatest == "yes":
    print("Downloading File...")
    wget.download("https://raw.githubusercontent.com/cat1554/dmr/main/latest.env","latest")
    print("Downloaded File!")
    latest = open("latest","r").read()
    print(f"Latest Version : {latest}")
    os.remove("latest")