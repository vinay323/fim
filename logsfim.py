import hashlib
import time
from datetime import datetime
from  tkinter import *
from tkinter import messagebox
root = Tk()
root.withdraw()


# List of files to monitor
file_paths = ['/home/vinay/Downloads/abc.txt','/home/vinay/Downloads/bcd.txt','/home/vinay/Downloads/pqr.txt']

# Dictionary to store the initial checksums
checksums = {}

# Calculate and store initial checksums
for file_path in file_paths:
    with open(file_path, 'rb') as file:
        contents = file.read()
        checksum = hashlib.sha256(contents).hexdigest()
        checksums[file_path] = checksum
        print(checksum)

# Create a log file
log_file = open('file_changes.log', 'a')

# Continuously monitor files
while True:
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            contents = file.read()
            checksum = hashlib.sha256(contents).hexdigest()
            if checksum != checksums[file_path]:
                messagebox.showwarning('alert title', 'File has been modified')
                messagebox.showinfo("MODIFIED FILE PATH",file)
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{current_time}: {file_path} has been modified!\n"
                print(log_entry)
                log_file.write(log_entry)
                # Take appropriate action here
                checksums[file_path] = checksum
    time.sleep(1)  # Wait for 1 second before checking files again
