
# This script is designed to read a log file and process its contents.
import os
import re
from pathlib import Path




def openLogFile(path, encoder='utf-8'):
    with open(path, "r") as file:
        try:
            # Iterate through each line in the file and yield it for processing
            for line in file:
                yield line
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
     

