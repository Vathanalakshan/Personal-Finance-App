"""Financial App"""
from dataclasses import dataclass
from dataclasses import field

from no_money_error import NoMoneyError

from finances.expense import Expense
from finances.income import Income
from finances.transaction import Transaction


@dataclass
class FinanceApp:
    """The Finance App that acts as your bank"""

    transactions: list[Transaction] = field(default_factory=list)
    funds: int = 0

    def event(self, transaction):
        """This method registers expenses and incomes in the financial app"""
        self.transactions.append(transaction)
        if isinstance(transaction, Income):
            self.funds += transaction.value
        elif isinstance(transaction, Expense):
            if self.funds < transaction.value:
                raise NoMoneyError(
                    f"You are missing {transaction.value-self.funds} euros"
                )
            self.funds -= transaction.value
        print("Your saving iss {self.funds}")

    def show_event_history(self):
        """This method prints out your finance app history"""
        print(self.transactions, sep="")
