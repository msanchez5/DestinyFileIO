# File path manipulation
import os
import hashlib

# This takes a filepath (fp) and returns a basename file name "mydata.txt"
path = "./example/mydata.txt"

def get_file_path_name(path):
    name = os.path.basename(path)
    return name

# This takes a filepath (fp) and returns a file size in bytes
def get_file_size(path):
    # path = get_file_path_name(path)
    size = os.path.getsize(path)
    #size = os.path.exists(path)
    return size

# This returns SHA1 digest for a file at the given getFilePathName
def convertSHA(path):
    f = open(path, 'r')
    str = f.read()
    str = str.strip( )
    str = str.encode('utf-8')
    f.close()
    sha = hashlib.sha1(str).hexdigest()
    return sha

# This returns MD5 digest for a file at the given getFilePathName
# def convertMD5():
# 	content = "The quick brown fox jumps over the lazy dog"
# 	encr = hashlib.md5(content)
# print encr.hexdigest()

print("Testing cases:")
print get_file_path_name(path)
print get_file_size(path)
print convertSHA(path)
