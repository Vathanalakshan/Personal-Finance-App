"""Income Module"""
from dataclasses import dataclass

from transaction import Transaction


@dataclass
class Income(Transaction):
    """Represents a income in your Financial App"""

    def __repr__(self) -> str:
        return f"Income of {self.message} of {self.value} euros on {self.date}\n"
