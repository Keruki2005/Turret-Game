"""#!/usr/bin/env python3
"""

import sys
import os
import subprocess
from pathlib import Path

# A small generic runner for the Turret-Game repository.
# It tries several heuristics to find the game's entrypoint and runs it
# with the current Python interpreter. This is intentionally conservative
# so it won't change your code structure. It just launches the game.

SEARCH_FILES = [
    "main.py",
    "turret.py",
    "game.py",
    "run.py",
    "app.py",
    "turret_game.py",
]

def find_entrypoint(root: Path):
    # 1) Look for an explicit file in root
    for name in SEARCH_FILES:
        p = root / name
        if p.is_file():
            return ("file", p)

    # 2) Look for a package with __main__.py
    for child in root.iterdir():
        if child.is_dir():
            mainpy = child / "__main__.py"
            if mainpy.is_file():
                return ("module", child.name)

    # 3) Look for any .py file that contains if __name__ == '__main__'
    for p in root.glob("*.py"):
        try:
            text = p.read_text(errors="ignore")
        except Exception:
            continue
        if "if __name__ == '__main__'" in text or 'if __name__ == "__main__"' in text:
            return ("file", p)

    return (None, None)

def run_file(path: Path, argv):
    cmd = [sys.executable, str(path)] + argv
    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd)

def run_module(module_name: str, argv):
    # Use -m to run package/module
    cmd = [sys.executable, "-m", module_name] + argv
    print(f"Running: {' '.join(cmd)}")
    return subprocess.call(cmd)

def main(argv):
    root = Path(__file__).parent.resolve()

    kind, thing = find_entrypoint(root)
    if kind == "file":
        return run_file(Path(thing), argv)
    elif kind == "module":
        return run_module(thing, argv)
    else:
        # As a last resort, try common subdirectories
        candidates = []
        for p in root.rglob("*.py"):
            candidates.append(p)
        print("Could not detect a canonical entrypoint for the game.")
        if candidates:
            print("Found some .py files in the tree — you can pass one as an argument:")
            for c in candidates[:50]:
                print(" - ", c.relative_to(root))
            print("To run a specific file: ./run_game.py path/to/file.py -- [game args]")
        else:
            print("No .py files were found in the repository root or subfolders.")
        return 2

if __name__ == '__main__':
    # Allow passing additional args after a "--" separator to forward to the game
    # e.g. ./run_game.py -- --level 2
    argv = []
    if "--" in sys.argv:
        idx = sys.argv.index("--")
        argv = sys.argv[idx+1:]
    # If the user provided a path to a python file as the first positional arg, run it
    if len(sys.argv) > 1 and sys.argv[1] != "--":
        first = Path(sys.argv[1])
        if first.exists() and first.suffix == ".py":
            sys.exit(run_file(first, sys.argv[2:]))
    sys.exit(main(argv))