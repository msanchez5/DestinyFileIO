import os
import unittest
from Python.DestinyFileIO import getFilePathName
from Python.DestinyFileIO import getFileSize
def testx(x):
    return x + 1

class MyTest(unittest.TestCase):
    def testGetFilename(self):
        self.assertEqual(getFilePathName("/Users/Marvin/Documents/Github/DestinyFileIO/Python/mydata.txt"), "mydata.txt")

    def testGetFilename(self):
        self.assertEqual(getFileSize("/Users/Marvin/Documents/Github/DestinyFileIO/Python/mydata.txt"), os.path.getsize("/Users/Marvin/Documents/Github/DestinyFileIO/Python/mydata.txt"))

if __name__ == '__main__':
    unittest.main()
