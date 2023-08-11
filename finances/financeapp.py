# finance/transaction.py
import pandas as pd
from no_money_error import NoMoneyError

from finances.expense import Expense
from finances.income import Income


class FinanceAPP:
    """
    Abstract Class to represent transactions
    """

    transactions = []
    funds = 0

    def __init__(self) -> None:
        pass

    # TO REFACTOR
    def show(self):
        for transaction in self.transactions:
            print(transaction)

    def add(self, transaction):
        self.transactions.append(transaction)
        if isinstance(transaction, Income):
            self.funds += transaction.value
        elif isinstance(transaction, Expense):
            if self.funds < transaction.value:
                raise NoMoneyError(
                    f"You are missing {transaction.value-self.funds} euros"
                )
            self.funds -= transaction.value
        print(self.funds)
