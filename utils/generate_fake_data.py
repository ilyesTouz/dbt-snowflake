import yaml
import random

import pandas as pd
import numpy as np
from faker import Faker


def generate_data(data: pd.DataFrame, nb_lines: int, yaml_path: str) -> pd.DataFrame:
    with open(yaml_path, 'r') as stream:
        country = yaml.safe_load(stream)

    doc_number = [
        f"0017{np.random.choice(np.arange(100, 400))}" for _ in range(nb_lines)]
    order_qty = [np.random.choice(np.arange(1, 400)) for _ in range(nb_lines)]
    billing_qty = order_qty
    doc_date = [Faker().date_time_between(start_date='-30y', end_date='now')
                for _ in range(nb_lines)]
    ship_to = [np.random.choice(country['0SHIP_TO__0INDUSTRY___T'])
               for _ in range(nb_lines)]
    sales_dist = [np.random.choice(
        country['GC_KUNNR__0SALES_DIST___T']) for _ in range(nb_lines)]
    countries = [np.random.choice(country['Country']) for _ in range(nb_lines)]

    # Columns
    columns = {'0DOC_NUMBER': doc_number,
               '0DOC_DATE': doc_date,
               'Order_Qty_New': order_qty,
               'Billing_Qty': billing_qty,
               '0SHIP_TO__0INDUSTRY___T': ship_to,
               'GC_KUNNR__0SALES_DIST___T': sales_dist,
               'Country': countries
               }

    return pd.DataFrame(columns)


if __name__ == '__main__':
    # Import data
    orders = pd.read_excel('./data/orders.xlsx')

    generate_data(data=orders, nb_lines=200, yaml_path='config.yaml').to_csv(
        './data/fake_orders.csv', sep=';')
