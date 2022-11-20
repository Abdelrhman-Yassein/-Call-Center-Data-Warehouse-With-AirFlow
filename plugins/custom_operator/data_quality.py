# Import Libraries and models
from airflow.hooks.mysql_hook import MySqlHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class DataQualityOperator(BaseOperator):
    """_summary_
        Create New Operator To Check Data Quality From Table After Insert
    Args:
        BaseOperator (Object): To Create To operator

    Raises:
        ValueError: Error Value
    """
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # operators params (with defaults) here
                 mysql_conn_id="",  # connection id  From admin connection
                 tables={},  # DataBase tables we will check
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params 
        self.mysql_conn_id = mysql_conn_id
        self.tables = tables

    def execute(self, context):
        """_summary_
            Data quality check for all tables 
            by count rows in every table
        """
        # Connect to MySQL by MySQL hook
        mysql_hook = MySqlHook(self.mysql_conn_id)

        # Iterat Tables To Check Every Table
        for table in self.tables:
            # Run Query To Check Tables Have Rows
            records = (mysql_hook
                       .get_records(f"SELECT COUNT(*) FROM {table}"))
            # Check If Records Have Values
            if len(records) < 1 or len(records[0]) < 1 :
                # If Table Not Have Any Value
                (self
                 .log
                 .error(f"Data quality check failed. {table} returned no results"))

                raise ValueError(
                    f"Data quality check failed. {table} returned no results")

            # If Table Have Data And Present Rows Number
            (self
             .log
             .info(f"Data quality on table {table} check passed with {records[0][0]} records"))

            # self.log.info('DataQualityOperator not implemented yet')
