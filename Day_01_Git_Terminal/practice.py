"""
Day 01 - Git & Terminal Practice Script
"""
import os
import subprocess

def check_git_status():
    """Checks if git is initialized and prints git status."""
    try:
        result = subprocess.run(["git", "status"], capture_output=True, text=True, check=True)
        print("--- Git Status ---")
        print(result.stdout)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Git is not initialized or git CLI is not found.")
        return False

def verify_day1_files():
    """Verifies Day 01 setup files exist."""
    base = os.path.dirname(__file__)
    required_files = ["README.md", "notes.txt", "reflection.txt"]
    print("--- Verifying Day 1 Files ---")
    for fname in required_files:
        fpath = os.path.join(base, fname)
        exists = os.path.exists(fpath)
        status = "EXISTS" if exists else "MISSING"
        print(f"File '{fname}': {status}")

if __name__ == "__main__":
    print("Checking Day 01 Git & Terminal Environment...\n")
    check_git_status()
    print()
    verify_day1_files()
