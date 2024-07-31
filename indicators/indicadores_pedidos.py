import pandas

from repository.postgres_repository import PostgresConsolidatedRepository


class OrderIndicators:
    def __init__(self, profile):
        self.consolidado_report = PostgresConsolidatedRepository(profile=profile)

    def get_total_orders(self, is_billed: bool = False) -> pandas.DataFrame:
        data = self.consolidado_report.order_indicators_per_client(is_billed=is_billed)
        orders_by_distributor = pandas.DataFrame(data)
        return orders_by_distributor


if __name__ == '__main__':
    indicadores_pedidos = OrderIndicators()
    indicadores_pedidos.get_total_orders()
