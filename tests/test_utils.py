#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_utils
----------------------------------

Tests for `utils` for the `cauldron` module.
"""

import unittest

from cauldron.utils import silence


class TestUtils(unittest.TestCase):
    def test_silence_silencing(self):
        self.assertEqual(
            True,
            silence(lambda x: x.startswith('foo'), range(5))
        )

    def test_silence_bool(self):
        self.assertEqual(
            False,
            silence(lambda x: x < 1, 5)
        )

    def test_silence_ret(self):
        self.assertEqual(
            25,
            silence(lambda x: x*x, 5, ret=True)
        )


if __name__ == '__main__':
    unittest.main()
