"""Main """
from datetime import datetime

from finance_app import FinanceApp

from finances.expense import Expense
from finances.income import Income


def main():
    """Command center where i run my app"""

    finance_app = FinanceApp()
    finance_app.run()


if __name__ == "__main__":
    main()
