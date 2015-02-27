import unittest

from .utils import silence


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
