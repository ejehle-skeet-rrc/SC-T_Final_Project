"""
Output Handler Module

This module has the OutputHandler class that writes financial data to CSV files.
It can write account summaries, suspicious transactions, and transaction stats
to separate files.

Classes:
    OutputHandler: Handles output of financial data to CSV files.

Author: "Kassius Jewar-Tessier"
Version: 1.0
Credits: COMP-1327 Faculty
"""
import csv

__author__ = "Kassius Jewar-Tessier"
__version__ = "1.0"
__credits__ = "COMP-1327 Faculty"

class OutputHandler:
    """
    A class that handles writing financial data to CSV files.

    This class takes financial data and writes it to CSV files. It can
    write account summaries, suspicious transactions, and transaction
    statistics to separate files.

    Attributes:
        __account_summaries (dict): Stores account summary data
        __suspicious_transactions (list): Stores suspicious transaction
            records
        __transaction_statistics (dict): Stores transaction statistics
    """

    def __init__(self, account_summaries: dict,
                       suspicious_transactions: list,
                       transaction_statistics: dict):
        """
        Initialize the OutputHandler with financial data.

        Args:
            account_summaries (dict): Account summary data with
                account numbers as keys
            suspicious_transactions (list): List of suspicious
                transaction records
            transaction_statistics (dict): Transaction statistics data
        """
        # Store the account summaries data
        self.__account_summaries = account_summaries
        # Store the suspicious transactions data
        self.__suspicious_transactions = suspicious_transactions
        # Store the transaction statistics data
        self.__transaction_statistics = transaction_statistics

    @property
    def account_summaries(self) -> dict:
        """
        Get the account summaries data.

        Returns:
            dict: The account summaries
        """
        return self.__account_summaries

    @property
    def suspicious_transactions(self) -> list:
        """
        Get the suspicious transactions data.

        Returns:
            list: The suspicious transactions
        """
        return self.__suspicious_transactions

    @property
    def transaction_statistics(self) -> dict:
        """
        Get the transaction statistics data.

        Returns:
            dict: The transaction statistics
        """
        return self.__transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Write account summaries data to a CSV file.

        This method creates a CSV file with account summary info
        including account number, balance, total deposits, and total
        withdrawals.

        Args:
            file_path (str): The path and filename where the CSV file
                will be created
        """
        # Open the file in write mode with newline='' to handle line endings properly
        with open(file_path, "w", newline="") as output_file:
            # Create a CSV writer object
            writer = csv.writer(output_file)
            # Write the header row with column names
            writer.writerow(["Account number",
                             "Balance",
                             "Total Deposits",
                             "Total Withdrawals"])

            # Iterate through each account in the summaries
            for account_number, summary in self.__account_summaries.items():
                # Write each account's data as a row in the CSV
                writer.writerow([account_number,
                                summary["balance"],
                                summary["total_deposits"],
                                summary["total_withdrawals"]])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        Write suspicious transactions data to a CSV file.

        This method creates a CSV file with suspicious transaction info
        including transaction ID, account number, date, type, amount,
        currency, and description.

        Args:
            file_path (str): The path and filename where the CSV file
                will be created
        """
        # Open the file in write mode with newline='' to handle line endings properly
        with open(file_path, "w", newline="") as output_file:
            # Create a CSV writer object
            writer = csv.writer(output_file)
            # Write the header row with column names
            writer.writerow(["Transaction ID",
                            "Account number",
                            "Date",
                            "Transaction type",
                            "Amount",
                            "Currency",
                            "Description"])

            # Iterate through each suspicious transaction
            for transaction in self.__suspicious_transactions:
                # Write each transaction's data as a row in the CSV
                writer.writerow([transaction["Transaction ID"],
                                transaction["Account number"],
                                transaction["Date"],
                                transaction["Transaction type"],
                                transaction["Amount"],
                                transaction["Currency"],
                                transaction["Description"]])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Write transaction statistics data to a CSV file.

        This method creates a CSV file with transaction statistics info
        including transaction type, total amount, and transaction count.

        Args:
            file_path (str): The path and filename where the CSV file
                will be created
        """
        # Open the file in write mode with newline='' to handle line endings properly
        with open(file_path, "w", newline="") as output_file:
            # Create a CSV writer object
            writer = csv.writer(output_file)
            # Write the header row with column names
            writer.writerow(["Transaction type",
                             "Total amount",
                             "Transaction count"])

            # Iterate through each transaction type and its statistics
            for transaction_type, statistic in self.__transaction_statistics.items():
                # Write each statistic's data as a row in the CSV
                writer.writerow([transaction_type,
                                 statistic["total_amount"],
                                 statistic["transaction_count"]])
