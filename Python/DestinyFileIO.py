# File path manipulation
import os
import hashlib
print("Welcome to DestinyFileIO")
# This takes a filepath (fp) and returns a basename file name "mydata.txt"
path = "/Users/Marvin/Documents/Github/DestinyFileIO/Python/mydata.txt"
def getFilePathName(path):
    path = os.path.basename(path)
    return path

# This takes a filepath (fp) and returns a file size in bytes
def getFileSize(path):
    file = os.path.getsize(path)
    return file

# This returns SHA1 digest for a file at the given getFilePathName
#def convertSHA(path):

# This returns MD5 digest for a file at the given getFilePathName
# def convertMD5():
# 	content = "The quick brown fox jumps over the lazy dog"
# 	encr = hashlib.md5(content)
# print encr.hexdigest()


print("Testing cases:")
print getFilePathName(path)
print getFileSize(path)
# print convertMD5()
