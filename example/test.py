import os
import unittest

from DestinyFileIO import get_file_path_name
from DestinyFileIO import get_file_size
from DestinyFileIO import convertSHA

class MyTest(unittest.TestCase):
    def test_file_name(self):
        self.assertEqual(get_file_path_name("mydata.txt"),
                         os.path.basename("mydata.txt"))

    def test_file_size(self):
        self.assertEqual(os.path.getsize("./example/mydata.txt"),
                        os.path.getsize("./example/mydata.txt"))

    def test_file_size(self):
        self.assertEqual(convertSHA("./example/mydata.txt"),
                        convertSHA("./example/mydata.txt"))

if __name__ == '__main__':
    unittest.main()
