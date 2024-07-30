from dataclasses import dataclass


@dataclass
class DatabaseConnectionData:
    dialect_driver: str = 'postgresql+psycopg2'
    user: str = ''
    password: str = ''
    host: str = ''
    port: str = ''
    database: str = ''
    schema: str = ''
