import unittest
from unittest.mock import patch
from io import StringIO
import pizza_order  # Import the script to test


class TestPizzaOrder(unittest.TestCase):
    @patch("builtins.input", side_effect=["S", "Y", "Y"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_small_pizza_with_pepperoni_and_cheese(self, mock_stdout, mock_input):
        # Run the pizza-order script
        pizza_order.main()
        output = mock_stdout.getvalue()
        self.assertIn("Your final bill is: $18.", output)

    @patch("builtins.input", side_effect=["M", "N", "Y"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_medium_pizza_with_cheese_only(self, mock_stdout, mock_input):
        pizza_order.main()
        output = mock_stdout.getvalue()
        self.assertIn("Your final bill is: $21.", output)

    @patch("builtins.input", side_effect=["L", "Y", "N"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_large_pizza_with_pepperoni_no_cheese(self, mock_stdout, mock_input):
        pizza_order.main()
        output = mock_stdout.getvalue()
        self.assertIn("Your final bill is: $28.", output)


if __name__ == "__main__":
    unittest.main()
