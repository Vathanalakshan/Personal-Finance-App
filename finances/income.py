from transaction import Transaction


class Income(Transaction):
    """
    Income
    """

    def __init__(self, message, value, date):
        self.message = message
        self.value = value
        self.date = date

    def __str__(self) -> str:
        return f"Income of {self.message} of {self.value} euros on {self.date}"
