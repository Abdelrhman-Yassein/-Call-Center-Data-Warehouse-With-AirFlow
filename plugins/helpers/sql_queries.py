class SqlQueries:

    # 1 - Extract And Insert Customer Data 
    customers_insert_table = """
    
        INSERT INTO customers(customer_name,city,state, sentiment)
        SELECT 
            customer_name,
            city,
            state,
            sentiment
        FROM
            staging_call
        WHERE
            id IS NOT NULL;

        """
    # 2 - Extract And Insert Fact_Call Table    
    fact_call_insert_table = """

        INSERT INTO call_fact(call_id,customer_id,call_date,csat_score,call_in_minutes)
        SELECT DISTINCT
            st.id as call_id,
            c.customer_id ,
            STR_TO_DATE(call_timestamp, '%m/%d/%Y') AS call_date,
            CASE
                WHEN st.csat_score = ' ' THEN 1
                WHEN st.csat_score = 0 THEN 1
            END AS  csat_score,
            call_minutes
        FROM 
            staging_call st
        join customers c 
        on st.customer_name = c.customer_name
        WHERE
            id IS NOT NULL;

        """
    # 3 - Extract And Insert call_time Table
    call_time_insert_table = """

        INSERT INTO call_time(call_date,day,week,weekday, month,year)
        SELECT DISTINCT
            STR_TO_DATE(call_timestamp, '%m/%d/%Y') AS call_date,
            DAY(STR_TO_DATE(call_timestamp, '%m/%d/%Y')) AS day,
            WEEK(STR_TO_DATE(call_timestamp, '%m/%d/%Y')) AS week,
            DAYNAME(STR_TO_DATE(call_timestamp, '%m/%d/%Y')) AS weekday,
            MONTH(STR_TO_DATE(call_timestamp, '%m/%d/%Y')) AS month,
            YEAR(STR_TO_DATE(call_timestamp, '%m/%d/%Y')) AS year
        FROM
            staging_call
        WHERE
            call_timestamp IS NOT NULL

        """
    # 4 - Extract And Insert call_info Table
    call_info_insert_table = """

        INSERT INTO call_info(call_id,reason,channel,call_center,response_time)
        SELECT DISTINCT
            id as call_id,
            reason,
            channel,
            call_center,
            response_time
        FROM 
            staging_call
        WHERE
            id IS NOT NULL;

            """
    # Extract Data From Csv File To Staging Table
    load_data_to_staging_call_table = """
    
            SET GLOBAL local_infile=1;
            LOAD DATA LOCAL INFILE '/opt/airflow/data/CallCenter.csv'
            INTO TABLE staging_call
            COLUMNS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            ESCAPED BY '"'
            LINES TERMINATED BY '\n'
            IGNORE 1 LINES;

            """
