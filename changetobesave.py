import hashlib
import time
import difflib
# Path of file to monitor
file_path = '/home/vinay/Downloads/abc.txt'

# Initial checksum of the file
initial_checksum = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()

# Continuously monitor the file
while True:
    current_checksum = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
    if current_checksum != initial_checksum:
        print("File has been modified!")
        # Calculate the changes made to the file
        with open(file_path, 'r') as f:
            old_contents = f.read()
        with open(file_path, 'r') as f:
            new_contents = f.read()
        diff = ''.join(list(difflib.unified_diff(old_contents.splitlines(1), new_contents.splitlines(1), n=0)))
        print(diff)
        print("Changes made to the file:\n{}".format(diff))
        # Update the initial checksum
        initial_checksum = current_checksum
    # Wait for 1 second before checking the file again
    time.sleep(1)
