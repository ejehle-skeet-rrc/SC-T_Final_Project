"""REQUIRED MODULE DOCUMENTATION"""

import unittest
from unittest import TestCase
from input_handler.input_handler import InputHandler
import json
from unittest.mock import patch, mock_open

__author__ = ""
__version__ = ""
__credits__ = "COMP-1327 Faculty"

class InputHandlerTests(TestCase):
    """Defines the unit tests for the InputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when testing the InputHandler class in 
        the tests that follow.
        
        Example:
            >>> data_processor = DataProcessor(self.FILE_CONTENTS)
        """
        
        self.FILE_CONTENTS = \
            ("Transaction ID,Account number,Date,Transaction type,"
            + "Amount,Currency,Description\n"
            + "1,1001,2023-03-01,deposit,1000,CAD,Salary\n"
            + "2,1002,2023-03-01,deposit,1500,CAD,Salary\n"
            + "3,1001,2023-03-02,withdrawal,200,CAD,Groceries")

    # Define unit test functions below

    def test_get_file_format_csv(self):

        #Arrange
        handler = InputHandler("test_data.csv")

        #Act & Assert
        result = handler.get_file_format()
        self.assertEqual(result, "csv")

    def test_get_file_format_json(self):
        #Arrange
        handler = InputHandler("test_data.json")

        #Act & Assert
        result= handler.get_file_format()
        self.assertEqual(result, "json")

    def test_read_csv_data_file_not_found(self):

        #Arrange
        handler = InputHandler("file_not_found.csv")

        #Act & assert
        with self.assertRaises(FileNotFoundError):
            handler.read_csv_data()

    def test_read_csv_data_returns_list(self):

        #Arrange 
        handler = InputHandler("input_data.csv")
        expected = [
            {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1000", "Currency": "CAD", "Description": "Salary"}, 
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"},
            {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
            "Transaction type": "withdrawal", "Amount": "200", "Currency": "CAD", "Description": "Groceries"}

        ]

        #ACT &Assert 
        with patch("builtins.open", mock_open(read_data=self.FILE_CONTENTS)):
            with patch("os.path.isfile", return_value=True):
                actual = handler.read_csv_data()

        self.assertEqual(expected, actual)
    
    def test_read_input_data_csv(self):

        #Arrange 
        handler = InputHandler("input_data.csv")
        expected = [
            {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1000", "Currency": "CAD", "Description": "Salary"}, 
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"},
            {"Transaction ID": "3", "Account number": "1001", "Date": "2023-03-02",
            "Transaction type": "withdrawal", "Amount": "200", "Currency": "CAD", "Description": "Groceries"}

        ]

        #ACT &Assert 
        with patch("builtins.open", mock_open(read_data=self.FILE_CONTENTS)):
            with patch("os.path.isfile", return_value=True):
                actual = handler.read_input_data()

        self.assertEqual(expected, actual)

    def test_read_input_data_json(self):

        #Arrange 
        handler = InputHandler("input_data.json")
        expected_json = [
            {"Transaction ID": "1", "Account number": "1001", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1000", "Currency": "CAD", "Description": "Salary"}, 
            {"Transaction ID": "2", "Account number": "1002", "Date": "2023-03-01",
            "Transaction type": "deposit", "Amount": "1500", "Currency": "CAD", "Description": "Salary"},
           
        ]

        #ACT &Assert 
        with patch("builtins.open", mock_open(read_data=json.dumps(expected_json))):
            with patch("os.path.isfile", return_value=True):
                actual = handler.read_input_data()

        self.assertEqual(expected_json, actual)

    def test_read_input_data_invalid(self):

        #Arrange
        handler = InputHandler("invalid_file.txt")
        expected = []

        #Act & Assert 
        with patch("os.path.isfile", return_value=True):
            actual = handler.read_input_data()
        self.assertEqual(expected, actual)
        

    


if __name__ == "__main__":
    unittest.main()
