from airflow import DAG
from postgres import DataTransferPostgres
from layers import *
from datetime import datetime
import yaml
import os


with open(os.path.join(os.path.dirname(__file__), 'schema.yaml'), encoding='utf-8') as f:
    YAML_DATA = yaml.safe_load(f)


DEFAULT_ARGS = {
    "owner": "airflow",
    "start_date": datetime(2021, 5, 31),
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
    "depends_on_past": True,
}



with DAG(
    dag_id="pg-data-flow8",
    default_args=DEFAULT_ARGS,
    schedule_interval="@once",
    max_active_runs=1,
    tags=['data-flow'],
) as dag1:
    sae = {
        table: DataTransferPostgres(
            query='select *,{job_id} from {table}',
            config=dict(
                table='sae.{table}'.format(table=table)
            ),
            task_id='sae_{table}'.format(table=table),
            source_pg_conn_str="host='db2' port=5432 dbname='my_database' user='root' password='postgres'",
            pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
            pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'"
        )
        for table in YAML_DATA['sources']['tables'].keys()
    }
    
    sal = {
        table: SalOperator(
            config=dict(
                target_table=table,
                source_table=table,
            ),
            task_id='sal_{table}'.format(table=table),
            pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
            pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'"
        )
        for table in YAML_DATA['sources']['tables'].keys()
    }

    for target_table, task in sal.items():
        sae[target_table] >> task
        


    hubs = {
        hub_name: {
            table: DdsHOperator(
                task_id='dds.h_{hub_name}_source_{source_table}'.format(hub_name=hub_name, source_table=table),
                config={
                    'hub_name': hub_name,
                    'source_table': table,
                    'bk_column': bk_column
                },
                pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'"
            )
            for table, cols in YAML_DATA['sources']['tables'].items()
            for col in cols['columns']
            for bk_column, inf in col.items()
            if inf.get('bk_for') == hub_name
        }
        for hub_name in YAML_DATA['groups']['hubs'].keys()
    }

    for hub, info in hubs.items():
        for source_table, task in info.items():
            sal[source_table] >> task
            
            
    links_h = {
        l_name: {
            table_name: DdsLHOperator(
                task_id='dds.l_{l_name}'.format(l_name=l_name),
                pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                config=dict(
                    link_name = l_name,
                    bk_columns = [key for a in cols['columns'] for key, value in a.items() ],
                    source_table=table_name,
                )
            )
            for table_name, cols in YAML_DATA['sources']['tables'].items()
            if table_name == info['source']
            
           
        }
        for l_name, info in YAML_DATA['groups']['links'].items()
        
    }

    for hub_names, info in links_h.items():
        for source_table, task in info.items():
            hub_names_list = hub_names.split('_')
            for a in hub_names_list:
                hubs[a][source_table] >> task
               
            
    links = {
        (l_hub_name, r_hub_name): {
            table_name: DdsLOperator(
                task_id='dds.l_{l_hub_name}_{r_hub_name}'.format(l_hub_name=l_hub_name, r_hub_name=r_hub_name),
                pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                config=dict(
                    l_hub_name=l_hub_name,
                    r_hub_name=r_hub_name,
                    l_bk_column=l_bk_column,
                    r_bk_column=r_bk_column,
                    source_table=table_name,
                )
            )
            for table_name, cols in YAML_DATA['sources']['tables'].items()
            for l_col in cols['columns']
            for l_bk_column, inf in l_col.items()
            if inf.get('bk_for') == l_hub_name
            for r_col in cols['columns']
            for r_bk_column, inf in r_col.items()
            if inf.get('bk_for') == r_hub_name
        }
        for r_hub_name, info in YAML_DATA['groups']['hubs'].items()
        for l_hub_name in info['links'].keys()
    }

    for (l_hub, r_hub), info in links.items():
        for source_table, task in info.items():
            hubs[l_hub][source_table] >> task
            hubs[r_hub][source_table] >> task
            
            
    satellites = {
        
            hub_name:{table:  DdsSOperator(
                task_id='dds.s_{hub_name}'.format(hub_name=hub_name),
                pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                config=dict(
                    hub_name = hub_name,
                    source_table = table,
                    bk_column = bk_column
                )
            )
            for table, cols in YAML_DATA['sources']['tables'].items()
            for col in cols['columns']
            for bk_column, inf in col.items()
            if inf.get('bk_for') == hub_name and table == hub_name
        }
        for hub_name, info in YAML_DATA['groups']['hubs'].items()
        for satellite_name in info['satellites'].keys()
    }
            
    for hub, info in satellites.items():
        for source_table, task in info.items():
            hubs[hub][source_table] >> task
            
            
    satellites_l = {
        
            link_name:{table:DdsSLOperator(
                task_id='dds.l_s_{link_name}'.format(link_name=link_name),
                pg_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                pg_meta_conn_str="host='db' port=5432 dbname='my_database' user='root' password='postgres'",
                config=dict(
                    link_name = link_name,
                    source_table = table,
                    bk_columns = [key for a in cols['columns'] for key, value in a.items() ]
                )
            )
            
            for table, cols in YAML_DATA['sources']['tables'].items()
            if table == info['source']
           
            
        }
        for link_name, info in YAML_DATA['groups']['links'].items()
        
    }
            
    for link, info in satellites_l.items():
        for source_table, task in info.items():
            links_h[link][source_table] >> task
    

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
