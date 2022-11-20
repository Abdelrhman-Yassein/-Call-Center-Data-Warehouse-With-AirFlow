# Import Libraries and Models
import logging
import datetime
from airflow import DAG
from helpers import CreateTables,SqlQueries
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from custom_operator.data_quality import DataQualityOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

# Default Argumant To Create DAG
default_args = {
    'owner': 'Abdelrhman Yassein',
    'start_date': datetime.datetime(2022, 11, 18),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}

# Create New Dag
dag = DAG(
    dag_id='Call_Center_ETL_DAG',
    default_args=default_args,
    description="Create Call Center Create Tables And ETL DATA",
    schedule_interval='@once' # Run One
)

# Create Start Task With No Thing Just Start
start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

# Create Mysql Operator To Drop All Tables
drop_tables = MySqlOperator(
    task_id="Drop_Tables",
    sql=CreateTables.drop_tables, # Drop Tables Statment Queries From  helpers -> create_tables_sql.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# Create Mysql Operator To Create Staging Table To Copy Data From csv File To Table 
create_staging_table = MySqlOperator(
    task_id='create_staging_table',
    sql=CreateTables.create_stage_table, # Create Table Statment Query From  helpers -> create_tables_sql.py
    mysql_conn_id='mysql_conn_id',# Connection Id From Admin -> Connection
    dag=dag
)

# Mysql Operator To Extract Data From CSV File To Staging Table 
load_data_to_staging_call_table = MySqlOperator(
    task_id='load_data_to_staging_call_table',
    sql=SqlQueries.load_data_to_staging_call_table,# Load Data To Staging Table Statment Query From  helpers -> sql_queries.py
    mysql_conn_id='mysql_conn_id',# Connection Id From Admin -> Connection
    dag=dag
)
# Mysql Operator To Create All Tables We Need
create_database_tables=MySqlOperator(
    task_id='create_database_tables',
    sql=CreateTables.create_tables_queries,# Create Tables  Statment Query From  helpers -> create_tables_sql.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# Mysql Operator To Extract Customers Data From Staging Table To Customres Table
insert_customer_data=MySqlOperator(
    task_id='insert_customer_data',
    sql=SqlQueries.customers_insert_table,# Extract Customers Data From Staging Table To Customres Table Query Statment From  helpers -> sql_queries.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# Mysql Operator To Extract fact_call Data From Staging Table To fact_call Table
insert_fact_call_data=MySqlOperator(
    task_id='insert_fact_call_data',
    sql=SqlQueries.fact_call_insert_table,# Extract fact_call Data From Staging Table To fact_call Table Query Statment From  helpers -> sql_queries.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# Mysql Operator To Extract call_time Data From Staging Table To call_time Table
insert_call_time_data=MySqlOperator(
    task_id='insert_call_time_data',
    sql=SqlQueries.call_time_insert_table,# Extract call_time Data From Staging Table To call_time Table Query Statment From  helpers -> sql_queries.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# Mysql Operator To Extract call_info Data From Staging Table To call_info Table
insert_call_info_data=MySqlOperator(
    task_id='insert_call_info_data',
    sql=SqlQueries.call_info_insert_table,# Extract call_info Data From Staging Table To call_info Table Query Statment From  helpers -> sql_queries.py
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    dag=dag
)

# DataQualityOperator To check Data Already Copy Or Not From -> plugins\custom_operator\data_quality.py
# Check Row Count
run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    mysql_conn_id="mysql_conn_id",# Connection Id From Admin -> Connection
    # Tables We Create Check For It
    tables=["customers", "call_fact", "call_time", "call_info"]
)

# Create End Task With No Thing Just End
end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

# AirFlow dependencies
start_operator>>drop_tables
drop_tables >> create_staging_table
create_staging_table >> load_data_to_staging_call_table
load_data_to_staging_call_table >> create_database_tables
create_database_tables >> insert_customer_data
insert_customer_data >> [insert_fact_call_data,insert_call_time_data,insert_call_info_data]
[insert_fact_call_data,insert_call_time_data,insert_call_info_data] >> run_quality_checks
run_quality_checks >> end_operator