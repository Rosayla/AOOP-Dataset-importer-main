import uuid


class Invoice:
    def __init__(self, invoice_no, invoice_date, total, customer,
                 payment, category, shopping_mall):
        self.invoice_id = uuid.uuid4()
        self.invoice_no = invoice_no
        self.invoice_date = invoice_date
        self.total = total
        self.customer = customer
        self.payment = payment
        self.category = category
        self.shopping_mall = shopping_mall
