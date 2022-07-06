import pip, os, sys, zipfile, shutil, time, platform
        
def get_consent(text): # function to get consent with y/n
    toreturn = 0
    consent = input(f"{text}\n(Y / N) > ")
    if consent == "yes" or consent == "y":
        toreturn = True
    else:
        toreturn = False
    return toreturn
        
if platform.system() == "Windows":
    print("Current Platform : Windows. Can Launch Program")
else:
    print("This updater script is currently only compatible with Windows Based Systems,\n A Mac And *nix Version Is Comming Soon™")
    print("Terminating in 15 Seconds")
    time.sleep(15)
    sys.exit("Invalid Platform")

try:
    import wget
except ImportError:
    pip.main(['install', wget])  

print("DMR Updater Script")

current_version = None
latest_version = None

try:
    versionfile = open("DMRPack\\version","r")
    current_version = versionfile.read()
    current_version = current_version.strip()
except FileNotFoundError: # except incorrect file 
    print("Could not find version file. Assuming version 0")
    current_version = 0


if get_consent("Do you want to obtain latest version?"):
    print("Downloading File...")
    wget.download("https://raw.githubusercontent.com/cat1554/dmr/main/latest","latest")
    latest_version = open("latest","r").read()
    latest_version = latest_version.strip()
    print(f"\n\n\nLatest Version : {latest_version} and current version = {current_version}")
    os.remove("latest")
    
if latest_version != current_version:
    print("Update Available")
    if get_consent("Install Update?"):
        print("Installing Update")
    else:
        print("Not Installing\nTerminating in 15 Seconds")
        time.sleep(15)
        sys.exit(0)
else: 
    print("You are on the latest version")
    if get_consent("Do you want to update anyways?"):
        print("Installing Update")
    else:
        print("Not Installing")
        time.sleep(15)
        sys.exit(0)

# install script 
print("Downloading Repository")
wget.download("https://github.com/cat1554/dmr/archive/refs/heads/main.zip","REPO.zip")

print("\nExtracting zip")
with zipfile.ZipFile(f"REPO.zip", 'r') as zip_ref:
    zip_ref.extractall(f"TEMPFOLDERREPO")
    
print("Deleting Old Texturepack")
try:
    shutil.rmtree("assets")
    print("Deleted assets")
    shutil.rmtree("extensions")
    print("Deleted extensions")
    os.remove("pack.mcmeta")
    print("Deleted pack.mcmeta")
    os.remove("pack.png")
    print("Deleted pack.png")
    os.remove("version")
    print("Deleted version")
    print("Deleted All Texturepack Files")
except OSError:
    print("No Need to delete old texturepack")

print("Moving TexturePack")
shutil.move("TEMPFOLDERREPO\\dmr-main\\DMRPack",".")



print("Cleaning Up")
shutil.rmtree("TEMPFOLDERREPO")
os.remove("REPO.zip")

print("Done Updating. Simply Reload textures in minecraft or launch the game! \a\a\a")

input("Press enter to exit.")

sys.exit()