import zipfile
import os
import sys

print("Starting Installation...")
try:
    import tarfile
    os.system("sudo apt-get install python3-pip")
    os.system("python3 -m pip install --upgrade pip")
    if (sys.version_info[0] < 3 or sys.version_info[1] < 5):
        print('Python version must be 3.5 or above')
        exit(1)
    # os.system("python3 -m pip install wheel")
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

print('Installing pip requirements ...')
os.system("pip3 install -r requirements.txt")


print("Downloading project files...")

project_url = 'https://github.com/a3har/MRDS/archive/master.zip'
download_file = requests.get(project_url)
open('project.zip', 'wb').write(download_file.content)
print("Project files Download Complete\nExtracting project files")
with zipfile.ZipFile('project.zip', 'r') as zip_ref:
    zip_ref.extractall('./temp')

os.remove('project.zip')

print('Downloading tesseract installation file')

tesseract_url = 'https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe'
r = requests.get(tesseract_url, allow_redirects=True)
open('tesseract.exe', 'wb').write(r.content)
