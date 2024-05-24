import os

import psycopg2
import psycopg2.extras


class DatabaseConnection:
    def __init__(self):
        psycopg2.extras.register_uuid()
        self.connection = psycopg2.connect(host='host.docker.internal', database=os.getenv('POSTGRES_DB'),
                                           user=os.getenv('POSTGRES_USER'), password=os.getenv('POSTGRES_PASSWORD'))

    def __enter__(self):
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.commit()
        self.connection.close()