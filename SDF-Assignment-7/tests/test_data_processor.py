"""This module contains the unit testing methods for the
    DataProcessor class from its respective module.

    Classes:
        DataProcessor: Processes the input data into 3 different
            statistic categories, which is returned to be outputted.
"""

import unittest, logging
from unittest import TestCase
from data_processor.data_processor import DataProcessor


__author__ = "Ethan Jehle-Skeet"
__version__ = "08.03.2025"
__credits__ = "COMP-1327 Faculty"

class TestDataProcessor(TestCase):
    """Defines the unit tests for the DataProcessor class."""

    def setUp(self):
        """This function is invoked before executing a unit test
        function.

        The following class attribute has been provided to reduce the 
        amount of code needed when creating DataProcessor class objects 
        in the tests that follow.  
        
        Example:
            >>> data_processor = DataProcessor(self.transactions)
        """
        
        self.transactions = [
            {
                "Transaction ID": "1",
                "Account number": "1001",
                "Date": "2023-03-01",
                "Transaction type": "deposit",
                "Amount": 1000,
                "Currency": "CAD",
                "Description": "Salary"
            }, 
            {
                "Transaction ID": "2",
                "Account number": "1004",
                "Date": "2023-03-01",
                "Transaction type": "withdrawal",
                "Amount": 500,
                "Currency": "CAD",
                "Description": "Groceries"
            },
            {
                "Transaction ID": "3",
                "Account number": "1002",
                "Date": "2023-03-02",
                "Transaction type": "withdrawal",
                "Amount": 15000,
                "Currency": "CAD",
                "Description": "House Down Payment"
            },
            {
                "Transaction ID": "4",
                "Account number": "1003",
                "Date": "2023-03-02",
                "Transaction type": "deposit",
                "Amount": 1250,
                "Currency": "XRP",
                "Description": "Salary"
            }
        ]

    # Define unit test functions below

    def test_data_processor_update_summaries_when_deposit(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
                "account_number": "1001",
                "balance": 1000.0,
                "total_deposits": 1000.0,
                "total_withdrawals": 0.0
            }
        # Act
        data_processor.process_data()

        actual = data_processor.account_summaries['1001']
        # Assert
        self.assertEqual(expected, actual)

    def test_data_processor_update_summary_when_withdrawal(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
                "account_number": "1004",
                "balance": -500.0,
                "total_deposits": 0.0,
                "total_withdrawals": 500.0
            }
        # Act
        data_processor.process_data()

        actual = data_processor.account_summaries['1004']
        # Assert
        self.assertEqual(expected, actual)

    def test_check_suspicious_transactions_greater_than_threshold(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
                "Transaction ID": "3",
                "Account number": "1002",
                "Date": "2023-03-02",
                "Transaction type": "withdrawal",
                "Amount": 15000,
                "Currency": "CAD",
                "Description": "House Down Payment"
        }
        # Act
        data_processor.process_data()

        actual = data_processor.suspicious_transactions[0]  
        # Assert
        self.assertEqual(expected, actual)

    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
                "Transaction ID": "4",
                "Account number": "1003",
                "Date": "2023-03-02",
                "Transaction type": "deposit",
                "Amount": 1250,
                "Currency": "XRP",
                "Description": "Salary"
            }
        # Act
        data_processor.process_data()

        actual = data_processor.suspicious_transactions[1]
        # Assert
        self.assertEqual(expected, actual)
        
    def test_check_suspicious_transactions_when_not_suspicious(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
                "Transaction ID": "2",
                "Account number": "1001",
                "Date": "2023-03-01",
                "Transaction type": "withdrawal",
                "Amount": 500,
                "Currency": "CAD",
                "Description": "Groceries"
            }
        # Act
        data_processor.process_data()

        actual = data_processor.suspicious_transactions
        # Assert
        self.assertNotIn(expected, actual)

    def test_update_transaction_statistics_deposit_stats(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = {
            "total_amount": 2250,
            "transaction_count": 2
        }
        # Act
        data_processor.process_data()
    
        actual = data_processor.transaction_statistics['deposit']
        # Assert
        self.assertEqual(expected, actual)

    def test_check_suspicious_transactions_logging(self):
        # Arrange
        data_processor = DataProcessor(self.transactions)

        expected = 1
        # Act and Assert
        with self.assertLogs() as captured:
            data_processor.check_suspicious_transactions(self.transactions[2])
        self.assertEqual(len(captured.records), expected)
        


if __name__ == "__main__":
    unittest.main()
