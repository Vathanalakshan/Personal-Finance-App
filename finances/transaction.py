"""Abstract parent class for expense and income """
from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction(ABC):
    """Transaction abstact class"""

    message: str
    value: int
    date: datetime
