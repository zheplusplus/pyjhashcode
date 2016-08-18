# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from jhashcode import hashcode

class TestStrings(unittest.TestCase):

    def test_empty_bytes(self):
        self.assertEqual(hashcode(b''), 0)

    def test_empty_unicode(self):
        self.assertEqual(hashcode(u''), 0)

    def test_bytes(self):
        self.assertEqual(hashcode(b'hello world'), 1794106052)

    def test_unicode(self):
        self.assertEqual(hashcode(u'者:s��2�*�=x�'), -1198738874)
        self.assertEqual(
            hashcode(u'僕と契約して、魔法少女になってほしい！'),
            640953514)

class TestInteger(unittest.TestCase):

    def test_int(self):
        self.assertEqual(hashcode(0), 0)
        self.assertEqual(hashcode(1), 1)
        self.assertEqual(hashcode(-1), -1)
