import uuid


class Payment:
    def __init__(self, payment_method, quantity, price):
        self.payment_id = uuid.uuid4()
        self.payment_method = payment_method,
        self.quantity = quantity,
        self.price = price
