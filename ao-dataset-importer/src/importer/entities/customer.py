import uuid


class Customer:
    def __init__(self, customer_no, gender, age):
        self.customer_id = uuid.uuid4()
        self.customer_no = customer_no
        self.gender = gender
        self.age = age
