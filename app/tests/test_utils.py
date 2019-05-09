"""Application test utils module."""

import unittest

from app.utils import generate_code


class TestAppUtilsModule(unittest.TestCase):
    def test_generate_code(self):
        untrimmed_code = 'ZTVmOWVjMDQ4ZDFkYmUxOWM3MGY3MjBlMDAyZjljYjE='

        code = generate_code('foo-bar')
        self.assertEqual(code, untrimmed_code[0:8])
        code = generate_code('foo-bar', 1)
        self.assertEqual(code, untrimmed_code[1:9])
        code = generate_code('foo-bar', 2)
        self.assertEqual(code, untrimmed_code[2:10])
        code = generate_code('foo-bar', 3)
        self.assertEqual(code, untrimmed_code[3:11])
