import uuid


class Category:
    def __init__(self, category):
        self.category_id = uuid.uuid4()
        self.category = category
