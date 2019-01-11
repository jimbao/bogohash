import unittest
import bogohash

class BogoTestCase(unittest.TestCase):

    def test_korv(self):
        mjau = bogohash.bogo("korv")
        self.assertEqual("****", mjau.digest())
