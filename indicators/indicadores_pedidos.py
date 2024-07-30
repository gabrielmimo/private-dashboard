import pandas

from repository.postgres_repository import PostgresConsolidatedRepository


class OrderIndicators:
    def __init__(self, profile):
        self.consolidado_report = PostgresConsolidatedRepository(profile=profile)

    def get_total_orders(self) -> pandas.DataFrame:
        data = self.consolidado_report.order_indicators_per_client()
        orders_by_distributor = pandas.DataFrame(data)
        print(orders_by_distributor)
        return orders_by_distributor


if __name__ == '__main__':
    indicadores_pedidos = OrderIndicators()
    indicadores_pedidos.get_total_orders()
