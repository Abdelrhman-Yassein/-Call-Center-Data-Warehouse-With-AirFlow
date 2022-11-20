class CreateTables:
    # Drop All Tables Queries
    drop_tables = """
    DROP TABLE IF EXISTS staging_call;
    DROP TABLE IF EXISTS call_info;
    DROP TABLE IF EXISTS call_fact;
    DROP TABLE IF EXISTS customers;
    DROP TABLE IF EXISTS call_time;
    """
    # Create Tables Queries
    create_tables_queries = """
    #Create Customer Tabel 

    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        customer_name VARCHAR(255) NOT NULL,
        city VARCHAR(50),
        state VARCHAR(50),
        sentiment VARCHAR(50)
    );

    # Create call_fact Table 

    CREATE TABLE IF NOT EXISTS call_fact (
        call_id VARCHAR(255) NOT NULL PRIMARY KEY,
        customer_id INT NOT NULL,
        call_date DATE NOT NULL,
        csat_score INT,
        call_in_minutes INT,
        constraint customer_fk foreign key (customer_id) references customers(customer_id) 
    );

    # Create call_time Table

    CREATE TABLE IF NOT EXISTS call_time (
            call_date   DATE NOT NULL primary key,
            day         INT NOT NULL,
            week        INT,
            weekday     VARCHAR(255),
            month       INT,
            year        INT
    );

    
    # Create call_info Table

    CREATE TABLE IF NOT EXISTS call_info (
        call_id VARCHAR(255) NOT NULL PRIMARY KEY,
        reason VARCHAR(255),
        channel VARCHAR(255),
        call_center VARCHAR(255),
        response_time VARCHAR(255)
    )
    """
    # Create Staging Table To Load Data From File To it
    create_stage_table = """
        create table staging_call(
            id              varchar(255),
            customer_name   varchar(255), 
            sentiment       varchar(255),
            csat_score      varchar(255),
            call_timestamp  varchar(255),
            reason          varchar(255),
            city            varchar(255),
            state           varchar(255),
            channel         varchar(255),
            response_time   varchar(255),
            call_minutes    int,
            call_center     varchar(255)
        );

    """
