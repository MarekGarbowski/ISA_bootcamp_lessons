from datetime import datetime


class Operation:
    def __init__(self, operation):
        self.operation = operation
        self.date = datetime.now()


