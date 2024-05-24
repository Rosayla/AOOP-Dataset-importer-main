import uuid


class ShoppingMall:
    def __init__(self, shopping_mall):
        self.shopping_mall_id = uuid.uuid4()
        self.shopping_mall = shopping_mall
