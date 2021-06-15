-- Sccsid:     @(#)dss_sal.ddl	2.1.8.1
CREATE TABLE sal.nation  ( nationkey  INTEGER NOT NULL,
                            name       CHAR(25) NOT NULL,
                            regionkey  INTEGER NOT NULL,
                            comment    VARCHAR(152),
							launch_id INTEGER NOT NULL);

CREATE TABLE sal.region  ( regionkey  INTEGER NOT NULL,
                            name       CHAR(25) NOT NULL,
                            comment    VARCHAR(152),
							launch_id INTEGER NOT NULL);

CREATE TABLE sal.part  ( partkey     INTEGER NOT NULL,
                          name        VARCHAR(55) NOT NULL,
                          mfgr        CHAR(25) NOT NULL,
                          brand       CHAR(10) NOT NULL,
                          type        VARCHAR(25) NOT NULL,
                          size        INTEGER NOT NULL,
                          container   CHAR(10) NOT NULL,
                          retailprice DECIMAL(15,2) NOT NULL,
                          comment     VARCHAR(23) NOT NULL,
						  launch_id INTEGER NOT NULL);

CREATE TABLE sal.supplier ( suppkey     INTEGER NOT NULL,
                             name        CHAR(25) NOT NULL,
                             address     VARCHAR(40) NOT NULL,
                             nationkey  INTEGER NOT NULL,
                             phone       CHAR(15) NOT NULL,
                             acctbal     DECIMAL(15,2) NOT NULL,
                             comment     VARCHAR(101) NOT NULL,
							 launch_id INTEGER NOT NULL);

CREATE TABLE sal.partsupp (  hashkey     INTEGER NOT NULL,
						     partkey     INTEGER NOT NULL,
                             suppkey     INTEGER NOT NULL,
                             availqty    INTEGER NOT NULL,
                             supplycost  DECIMAL(15,2)  NOT NULL,
                             comment     VARCHAR(199) NOT NULL,
							 launch_id INTEGER NOT NULL);

CREATE TABLE sal.customer (custkey    INTEGER NOT NULL,
                             name       VARCHAR(25) NOT NULL,
                             address    VARCHAR(40) NOT NULL,
                             nationkey   INTEGER NOT NULL,
                             phone       CHAR(15) NOT NULL,
                             acctbal     DECIMAL(15,2)   NOT NULL,
                             mktsegment  CHAR(10) NOT NULL,
                             comment     VARCHAR(117) NOT NULL,
							 launch_id INTEGER NOT NULL);

CREATE TABLE sal.orders  ( orderkey       INTEGER NOT NULL,
                           custkey        INTEGER NOT NULL,
                           orderstatus    CHAR(1) NOT NULL,
                           totalprice     DECIMAL(15,2) NOT NULL,
                           orderdate      DATE NOT NULL,
                           orderpriority  CHAR(15) NOT NULL,  
                           clerk          CHAR(15) NOT NULL, 
                           shippriority   INTEGER NOT NULL,
                           comment       VARCHAR(79) NOT NULL,
						   launch_id INTEGER NOT NULL);

CREATE TABLE sal.lineitem ( orderkey    INTEGER NOT NULL,
                             partkey     INTEGER NOT NULL,
                             suppkey     INTEGER NOT NULL,
                             linenumber  INTEGER NOT NULL,
                             quantity    DECIMAL(15,2) NOT NULL,
                             extendedprice  DECIMAL(15,2) NOT NULL,
                             discount    DECIMAL(15,2) NOT NULL,
                             tax         DECIMAL(15,2) NOT NULL,
                             returnflag  CHAR(1) NOT NULL,
                             linestatus  CHAR(1) NOT NULL,
                             shipdate    DATE NOT NULL,
                             commitdate  DATE NOT NULL,
                             receiptdate DATE NOT NULL,
                             shipinstruct CHAR(25) NOT NULL,
                             shipmode     CHAR(10) NOT NULL,
                             comment      VARCHAR(44) NOT NULL,
							 launch_id INTEGER NOT NULL);

