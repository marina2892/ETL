-- Sccsid:     @(#)dss_dds.ddl	2.1.8.1
create table dds.h_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(customer_bk)
);
create table dds.h_part (
    part_id SERIAL PRIMARY KEY,
    part_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(part_bk)
);
create table dds.h_supplier (
    supplier_id SERIAL PRIMARY KEY,
    supplier_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(supplier_bk)
);
create table dds.h_orders (
    orders_id SERIAL PRIMARY KEY,
    orders_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(orders_bk)
);
create table dds.h_nation (
    nation_id SERIAL PRIMARY KEY,
    nation_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(nation_bk)
);
create table dds.h_region (
    region_id SERIAL PRIMARY KEY,
    region_bk INTEGER,
    launch_id INTEGER,
    UNIQUE(region_bk)
);



create table dds.l_part_supplier (
    part_id INTEGER,
    supplier_id INTEGER,
	part_bk INTEGER,
    supplier_bk INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_part_supplier_orders (
    part_id INTEGER,
    supplier_id INTEGER,
	orders_id INTEGER,
	part_bk INTEGER,
	supplier_bk INTEGER,
	orders_bk INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_nation_supplier (
    nation_id INTEGER,
    supplier_id INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_customer_orders (
    customer_id INTEGER,
    orders_id INTEGER,
	customer_bk INTEGER,
	orders_bk INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_nation_customer (
    nation_id INTEGER,
    customer_id INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_region_nation (
    nation_id INTEGER,
    region_id INTEGER,
    launch_id INTEGER,
    effective_dttm timestamp default now()
);




create table dds.s_customer (
    customer_id INTEGER,
    name VARCHAR(25),
	address VARCHAR(40),
	phone CHAR(15),
	acctbal DECIMAL(15,2),
	mktsegment CHAR(10),
	comment VARCHAR(117),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);


create table dds.s_part (
    part_id INTEGER,
    name VARCHAR(55),
	mfgr CHAR(25),
	brand  CHAR(10),
	type        VARCHAR(25),
	size        INTEGER,
	container   CHAR(10),
	retailprice DECIMAL(15,2),
	comment     VARCHAR(23),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);


create table dds.s_supplier (
    supplier_id INTEGER,
    name        CHAR(25),
	address     VARCHAR(40),
	phone       CHAR(15),
	acctbal     DECIMAL(15,2),
	comment     VARCHAR(101),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);


create table dds.s_nation (
    nation_id INTEGER,
    name       CHAR(25),
	comment    VARCHAR(152),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);

create table dds.s_region (
    region_id INTEGER,
    name       CHAR(25),
	comment    VARCHAR(152),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);



create table dds.l_s_part_supplier (
    part_id INTEGER,
    supplier_id INTEGER,
	availqty    INTEGER,
	supplycost  DECIMAL(15,2),
	comment     VARCHAR(199),
    launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_s_part_supplier_orders (
    part_id INTEGER,
    supplier_id INTEGER,
	orders_id INTEGER,
	quantity    DECIMAL(15,2),
	extendedprice  DECIMAL(15,2),
	discount    DECIMAL(15,2),
	tax         DECIMAL(15,2),
	returnflag  CHAR(1),
	linestatus  CHAR(1),
	shipdate    DATE,
	commitdate  DATE,
	receiptdate DATE,
	shipinstruct CHAR(25),
	shipmode     CHAR(10),
	comment      VARCHAR(44),
	launch_id INTEGER,
    effective_dttm timestamp default now()
);
create table dds.l_s_customer_orders (
    customer_id INTEGER,
    orders_id INTEGER,
	orderstatus    CHAR(1),
	totalprice     DECIMAL(15,2),
	orderdate      DATE,
	orderpriority  CHAR(15),
	clerk          CHAR(15),
	shippriority   INTEGER,
	comment       VARCHAR(79),
	launch_id INTEGER,
    effective_dttm timestamp default now()
);


