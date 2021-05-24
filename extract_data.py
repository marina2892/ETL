import psycopg2

conn_string= "host='localhost' port=54320 dbname='my_database' user='root' password='postgres'"

with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY customer TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('customer.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY lineitem TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('lineitem.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY nation TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('nation.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY orders TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('orders.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY part TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('part.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY partsupp TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('partsupp.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY region TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('region.csv', 'w') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY supplier TO STDOUT WITH DELIMITER ',' CSV HEADER;"
    with open('supplier.csv', 'w') as f:
        cursor.copy_expert(q, f)
