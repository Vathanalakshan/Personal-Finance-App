"""Expense Module"""
from dataclasses import dataclass
from datetime import datetime

from transaction import Transaction


@dataclass
class Expense(Transaction):
    """Represents a expense in your Financial App"""

    message: str
    value: int
    date: datetime

    def __repr__(self) -> str:
        return f"Expense of {self.message} of {self.value} euros on {self.date} \n"
