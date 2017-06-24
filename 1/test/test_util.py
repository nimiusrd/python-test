import unittest
from util import util


class UtilTest(unittest.TestCase):
    def test_is_url(self):
        cases = [
            'http://example.com',
            'https://example.com',
            'https://e-ample.com',
            'https://e_ample.com',
            'https://ex/ample.com',
            'https://e%3ample.com',
            'http://example.com?q=hoge&p=fuga',
            'http://example.com#piyo',
        ]
        for case in cases:
            self.assertTrue(util.is_url(case))
