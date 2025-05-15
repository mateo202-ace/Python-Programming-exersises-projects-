import os
import re
from pathlib import Path


# defining the dummy log files
# INPUT_LOG_FILE = "/Users/juanmateo/Desktop/Security-Projects/Security-Projects/dummy_logs/auth.log"

script_dir = Path(__file__).resolve().parent
log_file_path = script_dir / "Practice_logs" / "auth.log"

failed_attempts_user = {}
failed_attempts_ip = {}


failed_attempts = []
with log_file_path.open("r") as file:
    for line in file:
        if "Failed password" in line:
            # Extract the user names
            match_user = re.search(r"(?<=user\s)(\S+)", line)
            if match_user:
                user = match_user.group(0)
                if user in failed_attempts_user:
                    failed_attempts_user[user] += 1
                else:
                    failed_attempts_user[user] = 1

            # Extract the IP address
            match_ip = re.search(r"(?<=from\s)(\S+)", line)
            if match_ip:
                ip = match_ip.group(0)
                if ip in failed_attempts_ip:
                    failed_attempts_ip[ip] += 1
                else:
                    failed_attempts_ip[ip] = 1

# Print the failed attempts
print("Failed login attempts by user:")
for user, count in failed_attempts_user.items():
    print(f"{user}: {count} failed attempts")

print("\nFailed login attempts by IP:")
for ip, count in failed_attempts_ip.items():
    print(f"{ip}: {count} failed attempts")

