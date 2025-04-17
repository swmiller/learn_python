import unittest
from caesar_cipher_2 import caesar


class TestCaesarCipher(unittest.TestCase):
    def test_encrypt(self):
        # Test basic encryption
        self.assertEqual(caesar("hello", 3, "encode"), "khoor")
        # Test wrapping around the alphabet
        self.assertEqual(caesar("xyz", 3, "encode"), "abc")
        # Test with non-alphabet characters
        self.assertEqual(caesar("hello, world!", 5, "encode"), "mjqqt, btwqi!")

    def test_decrypt(self):
        # Test basic decryption
        self.assertEqual(caesar("khoor", 3, "decode"), "hello")
        # Test wrapping around the alphabet
        self.assertEqual(caesar("abc", 3, "decode"), "xyz")
        # Test with non-alphabet characters
        self.assertEqual(caesar("mjqqt, btwqi!", 5, "decode"), "hello, world!")

    def test_large_shift(self):
        # Test large shift values
        self.assertEqual(caesar("hello", 29, "encode"), "khoor")  # 29 % 26 = 3
        self.assertEqual(caesar("khoor", 29, "decode"), "hello")  # 29 % 26 = 3

    def test_no_shift(self):
        # Test with no shift
        self.assertEqual(caesar("hello", 0, "encode"), "hello")
        self.assertEqual(caesar("hello", 0, "decode"), "hello")


if __name__ == "__main__":
    unittest.main()
