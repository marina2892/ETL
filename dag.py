from airflow import DAG
from postgres import DataTransferPostgres
from statistic import DataStatistic
from datetime import datetime
from airflow.sensors.external_task_sensor import ExternalTaskSensor



DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2021, 5, 31),
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": True,
}

with DAG(
    dag_id="pg_log",
    default_args=DEFAULT_ARGS,
    schedule_interval="@once",
    max_active_runs=1,
    tags=['data-flow'],
) as dag1:
    t1 = DataTransferPostgres(
        config=['public.customer','public.nation', 'public.region','public.lineitem','public.orders','public.part','public.partsupp','public.supplier'],
        query='select *, {job_id} from {table_name}',
        task_id='load',
        source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
        pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
        pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'"
    )
    s1 = ExternalTaskSensor(
             task_id="sensor_task1",
             external_dag_id=dag1.dag_id,
             external_task_id=t1.task_id,
             timeout=60,
             allowed_states=['success'],
             failed_states=['failed', 'skipped'],
             mode="reschedule",
    )
   
    t2 = DataStatistic(
        config={'table': 'nation','column':'n_name'},
        task_id='nation_st',
        pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
        pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'"
    )
    t1 >> s1 >> t2
    
    
    
    
