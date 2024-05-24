import uuid


class Gender:
    def __init__(self, gender):
        self.gender_id = uuid.uuid4()
        self.gender = gender
