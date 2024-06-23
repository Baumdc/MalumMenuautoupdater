import os
import requests
import zipfile
import shutil
import subprocess

# Download the ZIP file
url = "https://github.com/scp222thj/MalumMenu/archive/refs/heads/main.zip"
zip_path = "MalumMenu.zip"
with requests.get(url, stream=True) as r:
    with open(zip_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("MalumMenu")

# Build the project
project_path = "MalumMenu/MalumMenu-main"
subprocess.run(["dotnet", "build"], cwd=project_path, check=True)

# Define paths
dll_source_path = os.path.join(project_path, "src", "bin", "Debug", "net6.0", "MalumMenu.dll")
dll_destination_path = "[Amongusfolder]\\BepInEx\\plugins\\MalumMenu.dll"

# Move the DLL file and overwrite the existing one
shutil.move(dll_source_path, dll_destination_path)

# Clean up: remove the downloaded zip and the extracted folder
os.remove(zip_path)
shutil.rmtree("MalumMenu")

print("Operation completed successfully.")
