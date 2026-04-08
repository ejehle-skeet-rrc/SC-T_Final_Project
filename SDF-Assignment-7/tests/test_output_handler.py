"""
Test Output Handler Module

This module contains unit tests for the OutputHandler class.
It tests initialization, properties, and file writing methods.

Classes:
    TestOutputHandler: Test cases for the OutputHandler class.

Author: "Kassius Jewar-Tessier"
Version: 1.0
Credits: COMP-1327 Faculty
"""

from unittest import TestCase, main
from unittest.mock import patch, mock_open
from output_handler.output_handler import OutputHandler

__author__ = "Kassius Jewar-Tessier"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

class TestOutputHandler(TestCase):
    """Defines the unit tests for the OutputHandler class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attributes have been provided to reduce the 
        amount of code needed when creating OutputHandler class objects 
        in the tests that follow.  
        
        Example:
            >>> OutputHandler(self.account_summaries, 
                              self.suspicious_transactions, 
                              self.transaction_statistics)
        """
        
        self.account_summaries = { 
            "1001": {
                "account_number": "1001", 
                "balance": 50, 
                "total_deposits": 100, 
                "total_withdrawals": 50
            },
            "1002": {
                "account_number": "2", 
                "balance": 200, 
                "total_deposits": 200, 
                "total_withdrawals": 0
            }
        }

        self.suspicious_transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-14",
                "Transaction type": "deposit",
                "Amount": 250,
                "Currency": "XRP",
                "Description": "crypto investment"
            }
        ]

        self.transaction_statistics = {
            "deposit": {
                "total_amount": 300, 
                "transaction_count": 2
            }, 
            "withdrawal": {
                "total_amount": 50, 
                "transaction_count": 1
            }
        }

    def test_init(self):
        """Test that OutputHandler initializes correctly."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        # Test that object was created
        self.assertIsInstance(output_handler, OutputHandler)
    
    def test_account_summaries_property(self):
        """Test that account_summaries property returns the current state."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        # Test that property returns correct data
        self.assertEqual(output_handler.account_summaries, self.account_summaries)
    
    def test_suspicious_transactions_property(self):
        """Test that suspicious_transactions property returns the current state."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        # Test that property returns correct data
        self.assertEqual(output_handler.suspicious_transactions, self.suspicious_transactions)
    
    def test_transaction_statistics_property(self):
        """Test that transaction_statistics property returns the current state."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        # Test that property returns correct data
        self.assertEqual(output_handler.transaction_statistics, self.transaction_statistics)
    
    def test_write_account_summaries_to_csv(self):
        """Test that write_account_summaries_to_csv creates a file with expected number of rows."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        test_file_path = "test_account_summaries.csv"
        
        # Use mocking to test file writing without actually creating files
        with patch('builtins.open', mock_open()) as mocked_open:
            with patch('csv.writer') as mock_writer:
                mock_writer_instance = mock_writer.return_value
                output_handler.write_account_summaries_to_csv(test_file_path)
        
        # Check that open() was called with correct arguments
        mocked_open.assert_called_once_with(test_file_path, 'w', newline='')
        
        # Check that writerow() was called the expected number of times
        # (header row + 2 account rows = 3 total rows)
        self.assertEqual(mock_writer_instance.writerow.call_count, 3)
        
        # Check that the file was created (mocked)
        # This verifies the method creates a file at the specified path
        self.assertTrue(mocked_open.called)
        
        # Check that the correct content was written
        # Get the calls made to writerow and verify the data
        # Think of call_args_list like a filing cabinet with three drawers:
        # Drawer 1: Which row number (1st row, 2nd row, 3rd row)
        # Drawer 2: What type of information (the actual data vs extra info)
        # Drawer 3: The actual data list (the values that go in the CSV file)
        # 
        # When we write "calls[0][0][0]", we're saying:
        # - Go to the 1st row (calls[0])
        # - Get the actual data part (calls[0][0]) 
        # - Get the list of values (calls[0][0][0])
        calls = mock_writer_instance.writerow.call_args_list
        
        # Check header row (the row with column names like "Account number", "Balance", etc.)
        # This is like checking that the first row contains the correct column titles
        # calls[0] = "Go to the 1st row we wrote"
        # calls[0][0] = "Get the data part of that row"
        # calls[0][0][0] = "Get the actual list of column names"
        expected_header = ["Account number", "Balance", "Total Deposits", "Total Withdrawals"]
        self.assertEqual(calls[0][0][0], expected_header)
        
        # Check first account data (the row with account 1001's information)
        # This is like checking that the second row contains the correct account details
        # calls[1] = "Go to the 2nd row we wrote"
        # calls[1][0] = "Get the data part of that row"
        # calls[1][0][0] = "Get the actual list of account values"
        expected_account_1 = ["1001", 50, 100, 50]
        self.assertEqual(calls[1][0][0], expected_account_1)
        
        # Check second account data (the row with account 1002's information)
        # This is like checking that the third row contains the correct account details
        # calls[2] = "Go to the 3rd row we wrote"
        # calls[2][0] = "Get the data part of that row"
        # calls[2][0][0] = "Get the actual list of account values"
        expected_account_2 = ["1002", 200, 200, 0]
        self.assertEqual(calls[2][0][0], expected_account_2)
    
    def test_write_suspicious_transactions_to_csv(self):
        """Test that write_suspicious_transactions_to_csv creates a file with expected number of rows."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        test_file_path = "test_suspicious_transactions.csv"
        
        # Use mocking to test file writing without actually creating files
        with patch('builtins.open', mock_open()) as mocked_open:
            with patch('csv.writer') as mock_writer:
                mock_writer_instance = mock_writer.return_value
                output_handler.write_suspicious_transactions_to_csv(test_file_path)
        
        # Check that open() was called with correct arguments
        mocked_open.assert_called_once_with(test_file_path, 'w', newline='')
        
        # Check that writerow() was called the expected number of times
        # (header row + 1 transaction row = 2 total rows)
        self.assertEqual(mock_writer_instance.writerow.call_count, 2)
        
        # Check that the file was created (mocked)
        # This verifies the method creates a file at the specified path
        self.assertTrue(mocked_open.called)
        
        # Check that the correct content was written
        # Get the calls made to writerow and verify the data
        # Think of this like a recipe book where each recipe has ingredients:
        # - The recipe number (1st recipe, 2nd recipe)
        # - The ingredients section (vs cooking instructions)
        # - The actual list of ingredients
        # 
        # When we write "calls[0][0][0]", we're saying:
        # - Look at the 1st recipe (calls[0])
        # - Go to the ingredients section (calls[0][0])
        # - Get the list of ingredients (calls[0][0][0])
        calls = mock_writer_instance.writerow.call_args_list
        
        # Check header row (the row with column names like "Transaction ID", "Account number", etc.)
        # This is like checking that the first row has the right column titles
        # calls[0] = "Look at the 1st row we wrote"
        # calls[0][0] = "Get the data part of that row"
        # calls[0][0][0] = "Get the actual list of column names"
        expected_header = ["Transaction ID", "Account number", "Date", "Transaction type", "Amount", "Currency", "Description"]
        self.assertEqual(calls[0][0][0], expected_header)
        
        # Check transaction data (the row with the suspicious transaction details)
        # This is like checking that the second row has the right transaction information
        # calls[1] = "Look at the 2nd row we wrote"
        # calls[1][0] = "Get the data part of that row"
        # calls[1][0][0] = "Get the actual list of transaction values"
        expected_transaction = ["1", "1001", "2023-03-14", "deposit", 250, "XRP", "crypto investment"]
        self.assertEqual(calls[1][0][0], expected_transaction)
    
    def test_write_transaction_statistics_to_csv(self):
        """Test that write_transaction_statistics_to_csv creates a file with expected number of rows."""
        output_handler = OutputHandler(self.account_summaries, 
                                      self.suspicious_transactions, 
                                      self.transaction_statistics)
        test_file_path = "test_transaction_statistics.csv"
        
        # Use mocking to test file writing without actually creating files
        with patch('builtins.open', mock_open()) as mocked_open:
            with patch('csv.writer') as mock_writer:
                mock_writer_instance = mock_writer.return_value
                output_handler.write_transaction_statistics_to_csv(test_file_path)
        
        # Check that open() was called with correct arguments
        mocked_open.assert_called_once_with(test_file_path, 'w', newline='')
        
        # Check that writerow() was called the expected number of times
        # (header row + 2 transaction types = 3 total rows)
        self.assertEqual(mock_writer_instance.writerow.call_count, 3)
        
        # Check that the file was created (mocked)
        # This verifies the method creates a file at the specified path
        self.assertTrue(mocked_open.called)
        
        # Check that the correct content was written
        # Get the calls made to writerow and verify the data
        # Think of this like a library with three levels:
        # Level 1: Which book (1st book, 2nd book, 3rd book)
        # Level 2: Which chapter (the main content vs appendix)
        # Level 3: Which page (the actual information we want)
        # 
        # When we write "calls[0][0][0]", we're saying:
        # - Go to the 1st book (calls[0])
        # - Open the main chapter (calls[0][0])
        # - Turn to the page with the data (calls[0][0][0])
        calls = mock_writer_instance.writerow.call_args_list
        
        # Check header row (the row with column names like "Transaction type", "Total amount", etc.)
        # This is like checking that the first row has the right column titles
        # calls[0] = "Go to the 1st book (1st row)"
        # calls[0][0] = "Open the main chapter (data section)"
        # calls[0][0][0] = "Turn to the page with column names"
        expected_header = ["Transaction type", "Total amount", "Transaction count"]
        self.assertEqual(calls[0][0][0], expected_header)
        
        # Check deposit data (the row with deposit statistics)
        # This is like checking that the second row has the right deposit information
        # calls[1] = "Go to the 2nd book (2nd row)"
        # calls[1][0] = "Open the main chapter (data section)"
        # calls[1][0][0] = "Turn to the page with deposit data"
        expected_deposit = ["deposit", 300, 2]
        self.assertEqual(calls[1][0][0], expected_deposit)
        
        # Check withdrawal data (the row with withdrawal statistics)
        # This is like checking that the third row has the right withdrawal information
        # calls[2] = "Go to the 3rd book (3rd row)"
        # calls[2][0] = "Open the main chapter (data section)"
        # calls[2][0][0] = "Turn to the page with withdrawal data"
        expected_withdrawal = ["withdrawal", 50, 1]
        self.assertEqual(calls[2][0][0], expected_withdrawal)

if __name__ == "__main__":
    main()
