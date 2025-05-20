import unittest
from unittest.mock import patch
from io import StringIO
import ticket_booth  # Import the script to test


class TestTicketBooth(unittest.TestCase):
    @patch("builtins.input", side_effect=["130", "10", "N"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_child_ticket_no_photo(self, mock_stdout, mock_input):
        ticket_booth.main()
        output = mock_stdout.getvalue()
        self.assertIn("The ticket price based on your age is $5.", output)
        self.assertIn("Your final bill is $5.", output)

    @patch("builtins.input", side_effect=["130", "16", "Y"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_teen_ticket_with_photo(self, mock_stdout, mock_input):
        ticket_booth.main()
        output = mock_stdout.getvalue()
        self.assertIn("The ticket price based on your age is $7.", output)
        self.assertIn("Your final bill is $10.", output)

    @patch("builtins.input", side_effect=["130", "50", "N"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_free_ticket_age_45_to_55(self, mock_stdout, mock_input):
        ticket_booth.main()
        output = mock_stdout.getvalue()
        self.assertIn("The ticket price based on your age is $0.", output)
        self.assertIn("Your final bill is $0.", output)

    @patch("builtins.input", side_effect=["130", "25", "Y"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_adult_ticket_with_photo(self, mock_stdout, mock_input):
        ticket_booth.main()
        output = mock_stdout.getvalue()
        self.assertIn("The ticket price based on your age is $12.", output)
        self.assertIn("Your final bill is $15.", output)

    @patch("builtins.input", side_effect=["110"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_not_tall_enough(self, mock_stdout, mock_input):
        ticket_booth.main()
        output = mock_stdout.getvalue()
        self.assertIn("Sorry, you are not tall enough to ride the roller coaster.", output)
        self.assertIn("Here, have a lollipop to cheer you up!", output)


if __name__ == "__main__":
    unittest.main()