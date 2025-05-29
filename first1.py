import hashlib

def hash_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            return hashlib.sha256(content).hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Ask user for two file paths
file1 = input("Enter path to the first file: ")
file2 = input("Enter path to the second file: ")

# Compute hashes
hash1 = hash_file(file1)
hash2 = hash_file(file2)

# Compare and print result
if hash1 and hash2:
    if hash1 == hash2:
        print("The files are identical.")
    else:
        print("The files are different.")
