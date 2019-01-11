import unittest
import bogohash

class BogoTestCase(unittest.TestCase):

    def test_korv(self):
        mjau = bogohash.bogo("korv")
        self.assertEqual("****", mjau.digest())

    def test_update(self):
        mjau = bogohash.bogo("katt")
        mjau.update("lusse")
        self.assertEqual("*********", mjau.digest())
