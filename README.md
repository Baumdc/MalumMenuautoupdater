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

- Any [installed release build of MalumMenu](https://github.com/scp222thj/MalumMenu/releases/)
- [.NET SDK](https://dotnet.microsoft.com/download) installed and available in your PATH
- [Python 3](https://www.python.org/downloads/) installed and available in your PATH
- Python `requests` library (install with `pip install requests`)
- [Internet](https://en.wikipedia.org/wiki/Internet) connection to download the project files

## Installation

1. **Ensure you have [Python 3](https://www.python.org/downloads/) and the [.NET SDK](https://dotnet.microsoft.com/download) installed**:
   - Check Python installation:
     ```sh
     python --version
     ```
   - Check [.NET SDK](https://dotnet.microsoft.com/download) installation:
     ```sh
     dotnet --version
     ```

2. **Install the required [Python library](https://packaging.python.org/en/latest/tutorials/installing-packages/)**:
   ```sh
   pip install requests

3. **Download the Auto-Updater Script**
   Make shure "update_malummenu.py" & "mmAutoupdateStart.bat" are in the same folder

4. **Run `mmAutoupdateStart.bat`**
   It will promt you to put in the path of your Among us folder
   
   **You can find it here:**
   - Steam: Right-click Among Us in your Library → Click Manage → Click Browse local files.
   - Epic Launcher: Right-click Among Us in your Library → Click Manage → Click the folder icon in the Installation box.

## License
This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/Baumdc/MalumMenuautoupdater/blob/main/LICENSE) file for details.

Enjoy playing Among Us with the latest MalumMenu mod!

For any issues or questions, please open an [issue](https://github.com/scp222thj/MalumMenu/issues).
