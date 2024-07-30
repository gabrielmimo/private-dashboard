import os

from db.database_connection_data import DatabaseConnectionData
from db.sql.sql_connection import SQLConnection
from db.sql.models.consolidated.order_header import OrderHeader
from db.sql.models.consolidated.client import Client
from sqlalchemy import select, func, literal_column


class PostgresConsolidatedRepository:
    def __init__(self, profile: str):
        if any(env in profile for env in ['one', 'online', 'monster', 'xyz']):
            db_connection_data = DatabaseConnectionData(dialect_driver='postgresql+psycopg2',
                                                        user=os.getenv('PGSQL_AUTH_USER'),
                                                        password=os.getenv('PGSQL_AUTH_PASSWORD'),
                                                        host=os.getenv('PGSQL_AUTH_HOST'),
                                                        port=os.getenv('PGSQL_AUTH_PORT', 5432),
                                                        database=f"{profile.replace('nf-', 'nfi-')}consolidated-v37")
        else:
            db_connection_data = DatabaseConnectionData(dialect_driver='postgresql+psycopg2',
                                                        user=os.getenv('PGSQL_CONSOLIDATED_AUTH_USER'),
                                                        password=os.getenv('PGSQL_CONSOLIDATED_AUTH_PASSWORD'),
                                                        host=os.getenv('PGSQL_CONSOLIDATED_AUTH_HOST'),
                                                        port=os.getenv('PGSQL_CONSOLIDATED_AUTH_PORT'),
                                                        database=f"nfi-consolidated-v37")
        self.sql_connection = SQLConnection(db_connection_data)

    def get_nexon_nexoff_data(self, date_limit):
        with self.sql_connection.get_session() as session:
            query_select = select(OrderHeader.device, func.count().label('order_count'),
                                  func.sum(OrderHeader.total_with_taxes).label('total')) \
                .where(OrderHeader.created_at <= date_limit)
            query_1 = query_select.where(OrderHeader.user_role == 'CLIENT').add_columns(OrderHeader.user_role).group_by(
                OrderHeader.user_role, OrderHeader.device)
            query_2 = query_select.where(OrderHeader.user_role != 'CLIENT').add_columns(
                literal_column("'SELLER'").label('user_role2')).group_by('user_role2', OrderHeader.device)
            return session.execute(query_1.union(query_2)).mappings().all()

    def count_positivated_clients(self, interval_start, interval_end):
        with self.sql_connection.get_session() as session:
            query_select = select(func.count(OrderHeader.client_id.distinct()).label('client_count')) \
                .where(OrderHeader.created_at.between(interval_start, interval_end))
            query_1 = query_select.where(OrderHeader.user_role == 'CLIENT').add_columns(OrderHeader.user_role).group_by(
                OrderHeader.user_role)
            query_2 = query_select.where(OrderHeader.user_role != 'CLIENT').add_columns(
                literal_column("'SELLER'").label('user_role2')).group_by('user_role2')
            query_3 = query_select.add_columns(literal_column("'TOTAL'").label('user_role3')).group_by('user_role3')
            return session.execute(query_1.union(query_2, query_3)).mappings().all()

    def count_clients_by_created_at(self, date_limit):
        with self.sql_connection.get_session() as session:
            query_select = select(func.count(Client.id.distinct())).where(Client.created_at <= date_limit)
            return session.execute(query_select).scalar_one()

    def count_clients_by_registration_date(self, date_limit):
        with self.sql_connection.get_session() as session:
            query_select = select(func.count(Client.id.distinct())).where(Client.registration_date <= date_limit)
            return session.execute(query_select).scalar_one()

    def order_indicators_per_client(self, is_billed=False):
        with self.sql_connection.get_session() as session:
            query = select(
                OrderHeader.distributor_id,
                func.sum(OrderHeader.total).over(partition_by=OrderHeader.distributor_id).label('valor'),
                func.sum(OrderHeader.total_with_taxes).over(partition_by=OrderHeader.distributor_id).label(
                    'valor_com_taxa'),
                func.count(OrderHeader.id).over(partition_by=OrderHeader.distributor_id).label('qtd')).distinct()
            if is_billed:
                query = query.where(OrderHeader.order_status.in_(['BILLED', 'IN_TRANSIT', 'DELIVERED']))
            return session.execute(query).mappings().all()
