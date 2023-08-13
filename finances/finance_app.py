"""Financial App"""
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime

from negative_money_error import NegativeMoneyError
from no_money_error import NoMoneyError

from finances.expense import Expense
from finances.income import Income
from finances.transaction import Transaction


@dataclass
class FinanceApp:
    """The Finance App that acts as your bank"""

    transactions_history: list[Transaction] = field(default_factory=list)
    funds: int = 0

    def add_event(self, transaction: Transaction):
        """This method registers expenses and incomes in the financial app"""
        match transaction:
            case Income():
                self.funds += transaction.value
                self.transactions_history.append(transaction)
            case Expense():
                if self.funds < transaction.value:
                    try:
                        raise NoMoneyError(
                            f"You are missing {transaction.value-self.funds} euros"
                        )
                    except NoMoneyError as err:
                        print(err)
                        print("Action Aborted")
                else:
                    self.funds -= transaction.value
                    self.transactions_history.append(transaction)

    def show_event_history(self):
        """This method prints out your finance app history"""
        print(*self.transactions_history, sep="", end="")

    def show_savings(self):
        """This method prints out your savings"""
        print(f"Your savings is {self.funds} euros")

    def check_money(self, value: int) -> bool:
        """Check if negative value was submitted"""
        if value < 0:
            try:
                raise NegativeMoneyError()
            except NegativeMoneyError as err:
                print(err)
                return False

    def create_event(self):
        """This method create events"""
        event = input("Expense or Income : ")
        if event in ["Income", "Expense"]:
            value = int(input("Value : "))
            while (self.check_money(value)) is False:
                value = int(input("Value : "))
            message = input("Message : ")
            if event == "Expense":
                if self.add_event(Expense(value, message, datetime.now())):
                    print(f"Removed {value} euros from your account")
            elif event == "Income":
                self.add_event(Income(value, message, datetime.now()))
                print(f"Inserted {value} euros to your account")
        else:
            print("Wrong input please start again")

    def run(self):
        """Run your finance app"""
        while True:
            query = input("Savings or History or Action : ")
            if query == "Savings":
                self.show_savings()
            elif query == "History":
                self.show_event_history()
            elif query == "Action":
                self.create_event()
            elif query == "Q":
                print("Good Bye")
                break
            else:
                print("Wrong Input,Please Try Again ")
