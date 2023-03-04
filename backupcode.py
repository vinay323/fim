import hashlib
import os
import shutil
import time
import difflib
# List of files to monitor
file_paths = ['/home/vinay/Downloads/abc.txt', '/home/vinay/Downloads/bcd.txt', '/home/vinay/Downloads/pqr.txt']

# Create backup copies of the files
backup_paths = ['/path/to/backup1', '/path/to/backup2', '/path/to/backup3']
for i, file_path in enumerate(file_paths):
    shutil.copyfile(file_path, backup_paths[i])

# Initial checksums of the backup files
initial_checksums = []
for backup_path in backup_paths:
    initial_checksums.append(hashlib.sha256(open(backup_path, 'rb').read()).hexdigest())

# Continuously monitor the files
while True:
    for i, file_path in enumerate(file_paths):
        current_checksum = hashlib.sha256(open(backup_paths[i], 'rb').read()).hexdigest()
        if current_checksum != initial_checksums[i]:
            print("File {} has been modified!".format(file_path))
            # Calculate the changes made to the file
            with open(file_path, 'r') as f:
                old_contents = f.read()
            with open(backup_paths[i], 'r') as f:
                new_contents = f.read()
            diff = ''.join(list(difflib.unified_diff(old_contents.splitlines(1), new_contents.splitlines(1), n=0)))
            print("Changes made to file {}:\n{}".format(file_path, diff))
            # Update the initial checksum
            initial_checksums[i] = current_checksum
    # Wait for 1 second before checking the files again
    time.sleep(1)
