```markdown
# Installers for Turret-Game

This repository now includes simple installer scripts to create a Python virtual environment and install the runtime requirements (PyQt5) for each major OS.

Files added
- requirements.txt
- install_requirements_windows.bat
- install_requirements_linux.sh
- install_requirements_macos.sh

How to use
- Windows:
  1. Open a Command Prompt in the repository root.
  2. Run: install_requirements_windows.bat
  3. Activate the venv in the same command window before running the game:
     call venv\Scripts\activate
  4. Run the game:
     python "Turret Game1.py"

- Linux:
  1. Open a terminal in the repository root.
  2. Make the script executable (first time): chmod +x install_requirements_linux.sh
  3. Run: ./install_requirements_linux.sh
  4. Activate venv: source venv/bin/activate
  5. Run the game:
     python3 "Turret Game1.py"

- macOS:
  1. Open Terminal in the repository root.
  2. Make the script executable (first time): chmod +x install_requirements_macos.sh
  3. Run: ./install_requirements_macos.sh
  4. Activate venv: source venv/bin/activate
  5. Run the game:
     python3 "Turret Game1.py"

Notes & troubleshooting
- These scripts assume a working Python 3 interpreter in PATH (python on Windows, python3