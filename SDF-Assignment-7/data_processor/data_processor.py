"""Contains a class called DataProcessor which has multiple objects
and functions that provide the work of processing the provided
input data file information and returning three types of info
categories based on the data.

    Classes:
        DataProcessor: Processes the input data into 3 different
            statistic categories, which is returned to be outputted.
"""

import logging

__author__ = "Ethan Jehle-Skeet"
__version__ = "08.03.2025"
__credits__ = "COMP-1327 Faculty"

class DataProcessor:
    """Represents the data processor function of the main module,
    following the work of the input data class.
    """
    # Thereshold amount for Suspicious check usage later
    LARGE_TRANSACTION_THRESHOLD = 10000
    """Represents the maximum transaction threshold for
    suspcious activity detection.
    """
    # Threshold currency string for Suspicious check usage later
    UNCOMMON_CURRENCIES = ["XRP", "LTC"]
    """Represents the uncommon currencies to be checked for in
    the suspicious activity detection.
    """

    def __init__(self, transactions: list, 
                 log_file: str='',
                 logging_level: str = logging.WARNING,
                 logging_format: str = 
                 '%(asctime)s - %(message)s - %(levelname)s'):
        """Intialize a new object list of processed data taken from the
        various functions that create their info based on the input data
        provided.

        Now implemented default parameters for the logging configuration
        as well as defining the basicConfig() function for logging.

        Args:
            transactions (list): List of bank transactions 
                via input_file
            log_file (str): File location for logs to be saved.
            logging_level(str): Minimum level of log types to
                take in.
            logging_format(str): Format for logging to follow.
            

        """

        self.__transactions = transactions # List of transactions taken
        # from the input_handler and used as an argument for the class
        self.__account_summaries = {} # Dictionary of Account Summaries
        self.__suspicious_transactions = [] # List of Suspicious
                                            # Transactions
        self.__transaction_statistics = {} # Dictionary of Transaction
        logging.basicConfig(
            level= logging_level,
            filename = log_file,
            filemode = 'w',
            format = logging_format,
            datefmt='%m/%d/%Y - %H:%M'
            )
        
        self.logger = logging.getLogger(__name__)

    # Below is the Getter section, returning any of the class attributes
    # that the program or user requires.
    # Returns all of the labelled attributes from the __init__
    # Comments indicating the values

    @property
    def input_data(self) -> list:
        """Gets the input data of the DataProcessor class.

        Returns:
            list: The list of transactions from the input data.
        """

        return self.__transactions
    
    @property
    def account_summaries(self) -> dict:
        """Gets the account summaries dictionary created by the 
        DataProcessor class.

        Returns:
            dictionary: Dictionary of summaries based on the input data
            accounts.
        """

        return self.__account_summaries
    
    @property
    def suspicious_transactions(self) -> list:
        """Gets the dictionary of suspicious bank activites created
        by the functions of the DataProcessor class.
        
        Returns:
            list: List of the suspicious bank account activities
            based on the input data accounts.
        """

        return self.__suspicious_transactions
    
    @property
    def transaction_statistics(self) -> dict:
        """Gets the dictionary of Deposit/Withdrawal/Transfer stats
        created by the functions of the DataProcessor class.

        Returns:
            dictionary: Dictionary of the types of bank account
            activities and the times they occurred. 
        """

        return self.__transaction_statistics

    def process_data(self) -> dict:
        """Compiling the data that was individually processed through
        the three categories of information into one dictionary
        containing them all.
        
        Returns:
            dictionary: Dictionary of three information types based
                on the input data provided.
        """
        # Process data is the all-in-one method to be used for the main
        # module work, main module shouldn't be using the individual
        # processing methods unless for testing purposes.
        for transaction in self.__transactions:
            self.update_account_summary(transaction)
            self.check_suspicious_transactions(transaction)
            self.update_transaction_statistics(transaction)
        
        self.logger.info('Data Processing Complete')

        return {"account_summaries": self.__account_summaries,
                "suspicious_transactions": self.__suspicious_transactions,
                "transaction_statistics": self.__transaction_statistics}
        
    

    def update_account_summary(self, transaction: dict) -> None:
        """Updates the account summaries list in the object list of data
        to be processed, using info from the input file.

        Args:
            transaction (dictionary): Dictionary of bank transactions. 
        """

        account_number = transaction["Account number"]
        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])

        if account_number not in self.__account_summaries: 
            self.__account_summaries[account_number] = { 
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }
        # Above is the iteration that creates the dictionary of the
        # summary based on the transaction data.

        # Below is the transaction type check, followed by the stat
        # update using the amount float for both.

        if transaction_type == "deposit":
            self.__account_summaries[account_number]["balance"] += amount
            self.__account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self.__account_summaries[account_number]["balance"] -= amount
            self.__account_summaries[account_number]["total_withdrawals"] += amount

        self.logger.info(f'Account summary updated: {account_number}')

    def check_suspicious_transactions(self, transaction: dict) -> None:
        """Performs a check for suspcicious bank transactions by
        sifting through the input data provided in the
        list of transactions.
        
        Args:
            transaction (dictionary): Dictionary of bank transactions.

        Returns:
            None
        """

        amount = float(transaction["Amount"])
        currency = transaction["Currency"]
        # Here is the validation check for what will be considered
        # part of the suspicious transactions list
        if amount > self.LARGE_TRANSACTION_THRESHOLD \
            or currency in self.UNCOMMON_CURRENCIES:
            self.__suspicious_transactions.append(transaction)

        self.logger.warning(f'Suspicious Transaction: '
                            f'{transaction}')

    def update_transaction_statistics(self, transaction: dict) -> None:
        """Updates and tallies up the statistics of the three types
        of account activity based on the input data provided.
        
        Args:
            transaction (dictionary): Dictionary of bank transactions.
        
        Returns:
            None
        """

        transaction_type = transaction["Transaction type"]
        amount = float(transaction["Amount"])
        # Iteration to create dictionary of transaction statistics,
        # going through the list and ensuring there's no duplicates
        # in order to collect the data properly.
        if transaction_type not in self.__transaction_statistics:
            self.__transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self.__transaction_statistics[transaction_type]["total_amount"] += amount
        self.__transaction_statistics[transaction_type]["transaction_count"] += 1

        self.logger.info(f'Updated transaction statistics for:'
                         f' {transaction_type}')

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """Collects and creates an average transaction amount based
        on the input data provided, unused in main module work
        
        Args:
            transaction_type (str): String of transaction 
                type performed.

        Returns:
            float: average transaction amount calculated with
             total_amount / transaction_count
        """
        
        total_amount = self.__transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self.__transaction_statistics[transaction_type]["transaction_count"]
        # Average amount formula
        return 0 if transaction_count == 0 else total_amount / transaction_count
