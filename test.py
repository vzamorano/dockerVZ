import unittest
from app import welcome

class Testing(unittest.TestCase):
    def test_welcome(self):
        self.assertEqual(welcome(), 'Please go to the next direction => IP of your machine:9001/dockerEndpoint')

if __name__ == '__main__':
    unittest.main()