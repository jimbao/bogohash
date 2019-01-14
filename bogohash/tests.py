# -*- coding: utf-8 -*-

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

    # Test that H(a)+H(b)==H(b)+H(a)
    def test_commutative(self):
        s1 = "hoola"
        s2 = "bandoola"

        h1=bogohash.bogo(s1)
        h2=bogohash.bogo(s2)
        self.assertEqual(h1.digest()+h2.digest(), h2.digest()+h1.digest())

    # And would you know it, H(a)+H(b)==H(a+b)
    def test_distributive(self):
        s1 = "sparris"
        s2 = "bollar"

        h1 = bogohash.bogo(s1)
        h2 = bogohash.bogo(s2)
        h3 = bogohash.bogo(s1)
        h3.update(s2)
        self.assertEqual(h1.digest()+h2.digest(), h3.digest())

    # And while we're at it, also that H(a+b)==H(b+a). This follows as a logical consequence of the earlier two,
    # but we need to be thorough about these things
    def test_associative(self):
        s1 = "räksmörgås"
        s2 = "ålsås"

        h1 = bogohash.bogo(s1+s2)
        h2 = bogohash.bogo(s2+s1)
        self.assertEqual(h1.digest(), h2.digest())

    # And of course also H(a+0) == H(a)
    def test_identity(self):
        s1 = "sixteenasterisks"
        s2 = ""

        h1 = bogohash.bogo(s1 + s2)
        h2 = bogohash.bogo(s1)
        self.assertEqual(h1.digest(), h2.digest())
