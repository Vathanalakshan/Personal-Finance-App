"""Exception method to handle no money in the bank"""


class NoMoneyError(Exception):
    """Exception raised negative money.

    Attributes:
        money -- requested money which caused the error
        message -- explanation of the error
    """

    def __init__(self, message="You don't have enough money"):
        self.message = message
        super().__init__(self.message)
