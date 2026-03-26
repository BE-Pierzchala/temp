import os
import logging
import psycopg2

logger = logging.getLogger()

class SqlWorker:
    def __init__(self):
        self.schema = 'temp'
        self.connection = psycopg2.connect(
            database='dom',
            user=os.environ["READER"],
            password=os.environ["READER_PASSWORD"],
            host= os.environ["HOST"],
            port=5432,
        )

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.connection.close()

    def execute_query(self, query: str) -> str | None:
        """
        Wykonuje query i logguje wynik.
        """
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            logger.info(cursor.statusmessage)
            try:
                response = cursor.fetchall()
            except psycopg2.ProgrammingError:
                response = None
        for notice in self.connection.notices:
            logger.warning(notice.strip())
        self.connection.commit()
        return response

    def insert_data(self, temperature: float, humidity:float, ip: str) -> None:
        self.execute_query(f"INSERT INTO {self.schema}.data(temperature, humidity, ip) "
                           f"VALUES({temperature}, {humidity}, '{ip}');")
