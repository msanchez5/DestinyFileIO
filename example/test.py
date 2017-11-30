import os
import unittest

from DestinyFileIO import getFilePathName
from DestinyFileIO import getFileSize

class MyTest(unittest.TestCase):
    def testFileName(self):
        self.assertEqual(getFilePathName("./example/mydata.txt"), os.path.basename("./example/mydata.txt"))

    def testFileSize(self):
        self.assertEqual(getFileSize("./example/mydata.txt"), 44)

if __name__ == '__main__':
    unittest.main()
