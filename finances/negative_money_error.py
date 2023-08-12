"""Exception method to handle Negative money submitted"""


class NegativeMoneyError(Exception):
    """Exception raised cause negative money.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="You submitted a negative value"):
        self.message = message
        super().__init__(self.message)
