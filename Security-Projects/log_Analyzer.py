import os
import re


# defining the dummy log files
INPUT_LOG_FILE = "/Users/juanmateo/Desktop/Security-Projects/Security-Projects/dummy_logs/auth.log"


failed_attempts = []
with open(INPUT_LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:
            user_match = re.search(r"(?<=user\s)(\S+)", line) # Extract the username
            ip_match = re.search(r"(?<=from\s)(\S+)", line) # Extract the IP address

            if user_match and ip_match:
                failed_attempts.append({
                    "User" : user_match.group(0),
                    "IP" : ip_match.group(0)
                })
           
            
    
# Print the failed attempts
print("Failed login attempts:")
for attempt in failed_attempts:
    print(f"User: {attempt['User']} | IP: {attempt['IP']}")






   