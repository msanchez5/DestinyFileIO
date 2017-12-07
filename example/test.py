import os
import unittest

from example.DestinyFileIO import getFilePathName
from example.DestinyFileIO import getFileSize

class MyTest(unittest.TestCase):
    def test_file_name(self):
        self.assertEqual(getFilePathName("./example/mydata.txt"),
                         os.path.basename("./example/mydata.txt"))

    def test_file_size(self):
        self.assertEqual(getFileSize("./example/mydata.txt"), 44)

if __name__ == '__main__':
    unittest.main()
