# MalumMenuautoupdater
This is an inofficial autoupdate Program for the Among us cheat Malum Menu (https://github.com/scp222thj/MalumMenu)
This script automatically downloads, builds, and installs the latest version of the MalumMenu mod for Among Us.

## Overview

- [Requirements](#requirements)
- [Installation](#installation)
- [License](#license)



## Features

- Automatically downloads the latest version of MalumMenu
- Builds the project using .NET SDK
- Replaces the existing DLL in the Among Us plugins directory
- Cleans up temporary files

## Requirements

- [.NET SDK](https://dotnet.microsoft.com/download) installed and available in your PATH
- Python 3 installed and available in your PATH
- Python `requests` library (install with `pip install requests`)
- Internet connection to download the project files

## Installation

1. **Ensure you have Python and the .NET SDK installed**:
   - Check Python installation:
     ```sh
     python --version
     ```
   - Check .NET SDK installation:
     ```sh
     dotnet --version
     ```

2. **Install the required Python library**:
   ```sh
   pip install requests

3. **Download the Auto-Updater Script**
   Make shure "update_malummenu.py" & "mmAutoupdateStart.bat" are in the same folder

4. Open the update_malummenu.py file in a text editor.
    Locate the following line:
    `among_us_plugins_path = "D:\\SteamLibrary\\steamapps\\common\\Among Us\\BepInEx\\plugins\\MalumMenu.dll"`

6. Replace the path with the path to your Among Us BepInEx plugins directory.
   For example:
   ` among_us_plugins_path = "C:\\Games\\Among Us\\BepInEx\\plugins\\MalumMenu.dll"`
 Inshure that you use 2 backslash `\\` and not just one `\`

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/Baumdc/MalumMenuautoupdater/blob/main/LICENSE) file for details.

Enjoy playing Among Us with the latest MalumMenu mod!

For any issues or questions, please open an [issue](https://github.com/scp222thj/MalumMenu/issues).
