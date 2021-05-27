from airflow import DAG
from ps_hw import DataTransfer
from datetime import datetime


DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2021, 5, 26),
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": True,
}

with DAG(
    dag_id="dumps-data-flow",
    default_args=DEFAULT_ARGS,
    schedule_interval="@once",
    max_active_runs=1,
    tags=['data-flow'],
) as dag1:
    t1 = DataTransfer(
        filename='region.csv',
        query='select * from region',
        task_id='dump_region',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t2 = DataTransfer(
        filename='customer.csv',
        query='select * from customer',
        task_id='dump_customer',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t3 = DataTransfer(
        filename='nation.csv',
        query='select * from nation',
        task_id='dump_nation',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t4 = DataTransfer(
        filename='lineitem.csv',
        query='select * from lineitem',
        task_id='dump_lineitem',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t5 = DataTransfer(
        filename='orders.csv',
        query='select * from orders',
        task_id='dump_orders',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t6 = DataTransfer(
        filename='part.csv',
        query='select * from part',
        task_id='dump_part',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t7 = DataTransfer(
        filename='partsupp.csv',
        query='select * from partsupp',
        task_id='dump_partsupp',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    t8 = DataTransfer(
        filename='supplier.csv',
        query='select * from supplier',
        task_id='dump_supplier',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
    )
    
    t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8