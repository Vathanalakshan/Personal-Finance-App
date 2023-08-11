"""Income Module"""
from dataclasses import dataclass
from datetime import datetime

from transaction import Transaction


@dataclass
class Income(Transaction):
    """Represents a income in your Financial App"""

    message: str
    value: int
    date: datetime

    def __repr__(self) -> str:
        return f"Income of {self.message} of {self.value} euros on {self.date} \n"
