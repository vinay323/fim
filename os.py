import hashlib

file_path = '/home/vinay/Downloads/abc.txt'

# Get the initial checksum of the file
initial_checksum = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
print(initial_checksum)
# Open the file
with open(file_path, 'r') as f:
    contents = f.read()
    current_checksum = hashlib.sha256(contents.encode('utf-8')).hexdigest()
    print(current_checksum)
    if current_checksum != initial_checksum:
        print("WARNING: This file has been modified since it was last opened!")
        # Reset the initial checksum to the new value
        initial_checksum = current_checksum
    # Display the file contents
    print(contents)
