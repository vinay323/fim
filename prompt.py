import hashlib
import time

file_path = '/home/vinay/Downloads/abc.txt'

# Get the initial checksum of the file
initial_checksum = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()

# Continuously monitor the file
while True:
    with open(file_path, 'r') as f:
        contents = f.read()
        current_checksum = hashlib.sha256(contents.encode('utf-8')).hexdigest()
        if current_checksum != initial_checksum:
            print("File {} has been modified!".format(file_path))
            # Reset the initial checksum to the new value
            initial_checksum = current_checksum
    # Wait for 1 second before checking the file again
    time.sleep(1)
