#!/usr/bin/env bash
# macOS installer for Turret-Game requirements
# Usage: from repository root: chmod +x install_requirements_macos.sh && ./install_requirements_macos.sh

set -e

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. On macOS you can install it via Homebrew:"
  echo "    brew install python"
  echo "or download an installer from https://python.org"
  exit 1
fi

python3 -m venv venv
# Activate venv for this script
. venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Installation complete."
echo "Activate the virtual environment with:"
echo "    source venv/bin/activate"