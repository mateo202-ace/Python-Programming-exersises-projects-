
# This script is designed to read a log file and process its contents.
import os
import re
from pathlib import Path

script_dir = Path(__file__).resolve().parent
log_path = script_dir / "Practice_logs" / "auth.log"

def openLogFile(log_path, encoder='utf-8'):
    try:
        # Check if the file exists
        if not log_path.exists():
            raise FileNotFoundError(f"The log file does not exist: {log_path}")
        
        # Open the file and yield lines
        with log_path.open("r", encoding=encoder) as file:
            for line in file:
                yield line
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    
if __name__ == "__main__":
    print(f"Log file path: {log_path}")
    try:
        for line in openLogFile(log_path):
            print(line.strip())
    except Exception as e:
        print(f"An error occurred: {e}")