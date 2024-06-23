import os
import requests
import zipfile
import shutil
import subprocess

# Function to get Among Us folder path
def get_among_us_folder():
    config_file = "among_us_path.txt"
    
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            among_us_path = file.read().strip()
    else:
        among_us_path = input("Please enter the Among Us folder path (e.g., D:\\SteamLibrary\\steamapps\\common\\Among Us): ").strip()
        with open(config_file, "w") as file:
            file.write(among_us_path)
    
    return among_us_path

# Get the Among Us folder path
among_us_path = get_among_us_folder()
plugins_path = os.path.join(among_us_path, "BepInEx", "plugins")
dll_destination_path = os.path.join(plugins_path, "MalumMenu.dll")

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

# Define DLL source path
dll_source_path = os.path.join(project_path, "src", "bin", "Debug", "net6.0", "MalumMenu.dll")

# Move the DLL file and overwrite the existing one
shutil.copy(dll_source_path, dll_destination_path)

# Clean up: remove the downloaded zip and the extracted folder
os.remove(zip_path)
shutil.rmtree("MalumMenu")

print("Operation completed successfully.")
