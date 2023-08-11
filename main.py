"""Main """
from datetime import datetime

from financeapp import FinanceApp

from finances.expense import Expense
from finances.income import Income


def main():
    """Command center where i run my app"""

    finance_app = FinanceApp()
    finance_app.event(Income("Salaire", 111444, datetime(2020, 5, 17)))
    finance_app.event(Income("Salaire", 444, datetime(2020, 5, 17)))
    finance_app.event(Expense("Achate", 444, datetime(2020, 5, 17)))
    finance_app.event(Expense("Salaire", 444, datetime(2020, 5, 17)))
    finance_app.event(Expense("Salaire", 444, datetime(2020, 5, 17)))
    finance_app.event(Expense("Salaire", 444, datetime(2020, 5, 17)))
    finance_app.event(Income("Salaire", 444, datetime(2020, 5, 17)))
    finance_app.show_event_history()


if __name__ == "__main__":
    main()
