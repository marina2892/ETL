from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import csv
import psycopg2
from pathlib import Path

class DataTransfer(BaseOperator):
    @apply_defaults
    def __init__(self, source_pg_conn_str, query, filename, *args, **kwargs):
        super(DataTransfer, self).__init__(
            *args,
            **kwargs
        )
        self.source_pg_conn_str = source_pg_conn_str
        self.query = query
        self.filename = filename
        
    def provide_data(self, csv_file, context):
        self.log.info("context: {}".format(context))
        with psycopg2.connect(self.source_pg_conn_str) as conn, conn.cursor() as cursor:
            query_to_execute = self.query
            self.log.info("Executing query: {}".format(query_to_execute))
            cursor.execute(query_to_execute)
            csvwriter = csv.writer(
                csv_file,
                delimiter="\t",
                quoting=csv.QUOTE_NONE,
                lineterminator="\n",
                escapechar='\\'
            )

            while True:
                cursor.arraysize = 1000
                rows = cursor.fetchmany()
                if rows:
                    self.log.info("fetchall: {}".format(rows))
                    for row in rows:
                        _row = list(row)
                        csvwriter.writerow(_row)
                else:
                    break
                
        
    def execute(self, context):
        save_path = Path(__file__).parent.joinpath('dumps')
        if not save_path.exists():
            save_path.mkdir()
        file_path = save_path.joinpath(self.filename)
        self.log.info("filepath: {}".format(file_path))
        with open(file_path, "w", encoding="utf-8") as csv_file:
            self.provide_data(csv_file, context)

        self.log.info("writing succed")
            
            
            
                
