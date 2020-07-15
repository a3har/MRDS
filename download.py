import zipfile
import os
import sys

print("Starting Installation...")

try:
    import tarfile
    os.system("python3 -m pip install requests")
except:
    print("Intialization Failed.")
    exit(1)

try:
    import requests
except:
    print("\n\nPlease restart the same code once again!")
    exit(1)


print("Initalized")


print("Downloading project files...")

project_url = 'https://github.com/a3har/MRDS/archive/master.zip'
download_file = requests.get(project_url)
open('project.zip', 'wb').write(download_file.content)
print("Project files Download Complete\nExtracting project files")
with zipfile.ZipFile('project.zip', 'r') as zip_ref:
    zip_ref.extractall('./')

os.remove('project.zip')
