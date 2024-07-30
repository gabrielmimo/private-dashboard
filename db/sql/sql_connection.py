import sqlalchemy
from sqlalchemy.orm import sessionmaker

from db.database_connection_data import DatabaseConnectionData


class SQLConnection:

    def __init__(self, database_connection_data: DatabaseConnectionData):
        if database_connection_data.user:
            config = f"{database_connection_data.dialect_driver}://{database_connection_data.user}:{database_connection_data.password}" \
                     f"@{database_connection_data.host}:{database_connection_data.port}/{database_connection_data.database}"
        else:
            config = f"{database_connection_data.dialect_driver}://{database_connection_data.host}:{database_connection_data.port}/" \
                     f"{database_connection_data.database}"

        self.engine = sqlalchemy.create_engine(config, pool_size=5, max_overflow=5)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def execute_raw_sql_statement(self, raw_sql_statement: str):
        with self.get_session() as session:
            result = session.execute(sqlalchemy.text(raw_sql_statement))
        return result.mappings()

    def execute_commit_raw_sql_statement(self, raw_sql_statement: str):
        with self.get_session() as session:
            session.execute(sqlalchemy.text(raw_sql_statement))
            session.commit()
