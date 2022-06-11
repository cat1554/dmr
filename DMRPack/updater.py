#Set to True if need debug messages
ENABLE_DEBUG = False

import os
import time
import sys
import wget
import zipfile


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
#fuck this i give up on comments
latest = None

obtainlatest = input(f"Obtain Latest Version Info \n(Will Download Temporary File named \"latest\" into {os.getcwd()} IF THIS FILE ALEREADY EXISTS IT WILL GET CORRUPTED) \n(Y / N) > ")
if obtainlatest == "y" or obtainlatest == "yes":
    print("Downloading File...")
    wget.download("https://raw.githubusercontent.com/cat1554/dmr/main/latest","latest")
    latest = open("latest","r").read()
    print(f"\n\n\nLatest Version : {latest}")
    os.remove("latest")
else:
    sys.exit(0)

installupdate = None

if version != latest:
    print("Update Found !")
    installupdate = input("Install Update? > ")
else:
    print("You are up to date, No Need to update")
    print("TIP : If your pack is corrupted, simply change the contents of the version files and run me again")
    time.sleep(100)
    sys.exit

latest = "1"
if installupdate == "yes" or installupdate == "y":
    os.chdir("..")
    print("Dowloading Zip...")
    wget.download(f"https://github.com/cat1554/dmr/releases/download/{latest}/DMRPack.zip",f"DMRPACK{latest}.zip")
    print(" Done!")
    print("Extracting zip")
    with zipfile.ZipFile(f"DMRPACK{latest}.zip", 'r') as zip_ref:
        zip_ref.extractall(f"DMRPack V{latest}")
    print("Done!")
    print("Deleting Zip")
    os.remove(f"DMRPACK{latest}.zip")
    print("Done!")
    print("\n\n\nTexture Pack Updated!. \nSimply load the new version on minecraft")
else:
    print("Download Cancelled!")
    time.sleep(100)
    sys.exit(1)