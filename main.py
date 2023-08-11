import datetime

import numpy as np
from financeapp import FinanceAPP

from finances.expense import Expense
from finances.income import Income


def main():
    finance_app = FinanceAPP()
    finance_app.add(Income("Salaire", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Income("Salaire", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Expense("Achate", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Expense("Salaire", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Expense("Salaire", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Expense("Salaire", 444, datetime.datetime(2020, 5, 17)))
    finance_app.add(Income("Salaire", 444, datetime.datetime(2020, 5, 17)))


if __name__ == "__main__":
    main()
