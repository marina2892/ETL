from data_transfer import DataTransfer
import csv
import psycopg2


class DataTransferPostgres(DataTransfer):
    def __init__(
        self, source_pg_conn_str, pg_conn_str, pg_meta_conn_str, query, config, *args, **kwargs
    ):
        super(DataTransferPostgres, self).__init__(
            pg_conn_str=pg_conn_str, config=config,pg_meta_conn_str=pg_meta_conn_str, *args, **kwargs
        )
        self.source_pg_conn_str = source_pg_conn_str
        self.query = query

    def provide_data(self, csv_file, context):
        pg_conn = psycopg2.connect(self.source_pg_conn_str)
        pg_cursor = pg_conn.cursor()
        query_to_execute = (self.query).format(job_id = context["task_instance"].job_id,table_name = self.config['table'])
        self.log.info("Executing query: {}".format(query_to_execute))
        pg_cursor.execute(query_to_execute)
        csvwriter = csv.writer(
            csv_file,
            delimiter="\t",
            quoting=csv.QUOTE_NONE,
            lineterminator="\n",
            escapechar='\\'
        )

        while True:
            pg_cursor.arraysize = 1000
            rows = pg_cursor.fetchmany()
            if rows:
                for row in rows:
                    _row = list(row)
                    csvwriter.writerow(_row)
            else:
                break
        pg_conn.close()