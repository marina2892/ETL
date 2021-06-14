import psycopg2

conn_string= "host='localhost' port=5433 dbname='my_database' user='root' password='postgres'" 

with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY customer from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/customer.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY lineitem from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/lineitem.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY nation from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/nation.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY orders from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/orders.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY part from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/part.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY partsupp from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/partsupp.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY region from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/region.csv', 'r') as f:
        cursor.copy_expert(q, f)
        
with psycopg2.connect(conn_string) as conn, conn.cursor() as cursor:
    q = "COPY supplier from STDIN WITH DELIMITER ',' CSV HEADER;"
    with open('table/supplier.csv', 'r') as f:
        cursor.copy_expert(q, f)
