import os
import subprocess

def install_requirements():
    """Install required packages from requirements.txt."""
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def run_sorter():
    """Run the sorter.py script."""
    subprocess.check_call([os.sys.executable, 'sorter.py'])

if __name__ == "__main__":
    install_requirements()
    run_sorter()
