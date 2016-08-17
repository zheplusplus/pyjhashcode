# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from jhashcode import hashcode

class TestJHashCode(unittest.TestCase):

    def test_empty_bytes(self):
        self.assertEqual(hashcode(b''), 0)

    def test_empty_unicode(self):
        self.assertEqual(hashcode(u''), 0)

    def test_unicode(self):
        self.assertEqual(hashcode(u'者:s��2�*�=x�'), -1198738874)
