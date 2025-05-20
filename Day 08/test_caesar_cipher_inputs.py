import unittest
from unittest.mock import patch
from caesar_cipher_2 import get_direction, get_text, get_shift


class TestCaesarCipherInputs(unittest.TestCase):
    @patch("builtins.input", side_effect=["encode"])
    def test_get_direction_encode(self, mock_input):
        self.assertEqual(get_direction(), "encode")

    @patch("builtins.input", side_effect=["decode"])
    def test_get_direction_decode(self, mock_input):
        self.assertEqual(get_direction(), "decode")

    @patch("builtins.input", side_effect=["invalid", "encode"])
    def test_get_direction_invalid_then_valid(self, mock_input):
        self.assertEqual(get_direction(), "encode")

    @patch("builtins.input", side_effect=["Hello, World!"])
    def test_get_text(self, mock_input):
        self.assertEqual(get_text(), "hello, world!")

    @patch("builtins.input", side_effect=["", "  ", "Valid message"])
    def test_get_text_empty_then_valid(self, mock_input):
        self.assertEqual(get_text(), "valid message")

    @patch("builtins.input", side_effect=["5"])
    def test_get_shift_valid(self, mock_input):
        self.assertEqual(get_shift(), 5)

    @patch("builtins.input", side_effect=["-1", "27", "10"])
    def test_get_shift_invalid_then_valid(self, mock_input):
        self.assertEqual(get_shift(), 10)

    @patch("builtins.input", side_effect=["invalid", "15"])
    def test_get_shift_non_integer_then_valid(self, mock_input):
        self.assertEqual(get_shift(), 15)


if __name__ == "__main__":
    unittest.main()
