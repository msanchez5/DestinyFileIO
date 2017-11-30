# File path manipulation
import os

# This takes a filepath (fp) and returns a basename file name "mydata.txt"
fp = "/home/kim/mydata.txt"
def getFilePathName(path):
    path = os.path.basename(path)
    return path
# This takes a filepath (fp) and returns a file size in bytes
# def getFileSize(path):
# This returns SHA1 digest for a file at the given getFilePathName
#def convertSHA(path):
# This returns MD5 digest for a file at the given getFilePathName
#def convertMD5(path):
