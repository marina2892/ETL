import logging
import os
import time
import datetime
import psycopg2
from contextlib import contextmanager
from airflow.utils.decorators import apply_defaults
from utils import DataFlowBaseOperator

class DataStatistic(DataFlowBaseOperator): 
    @apply_defaults
    def __init__(self, config, pg_conn_str, pg_meta_conn_str, *args, **kwargs):
        super(DataStatistic, self).__init__(
            pg_meta_conn_str=pg_meta_conn_str,
            *args,
            **kwargs
        )
        self.config = config
        self.pg_conn_str = pg_conn_str
        
    def execute(self, context):
        with psycopg2.connect(self.pg_meta_conn_str) as conn, conn.cursor() as cursor:
            cursor.execute(
                """
            select target_launch_id from log order by processed_dttm desc limit 1
               ;
            """
            )
            result3 = cursor.fetchone()
        self.config.update( 
            launch_id = result3[0]
        )
        with psycopg2.connect(self.pg_conn_str) as conn, conn.cursor() as cursor:
            cursor.execute(
                """
            select count({column}) from {table} where {column} is null and launch_id = {launch_id}
               ;
            """.format(
                    **self.config
                )
            )
            result1 = cursor.fetchone()
        with psycopg2.connect(self.pg_conn_str) as conn, conn.cursor() as cursor:
            cursor.execute(
                """
            select count({column}) from {table} where launch_id = {launch_id}
               ;
            """.format(
                    **self.config
                )
            )
            result2 = cursor.fetchone()
        
        
        self.config.update( 
            
            cnt_nulls = result1[0],
            cnt_all = result2[0],
            
             
        )
        self.write_etl_statistic(self.config)