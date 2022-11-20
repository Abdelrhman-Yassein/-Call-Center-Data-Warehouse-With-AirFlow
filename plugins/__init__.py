# Import Libraries And Model
from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin
# Import From -> plugins\custom_operator
import custom_operator
# Import From -> plugins\helpers
import helpers

# Defining the plugin class
class UdacityPlugin(AirflowPlugin):
    name = "plugins"
    operators = [
        # Class From plugins\custom_operator\data_quality.py -> DataQualityOperator
        custom_operator.DataQualityOperator
    ]
    helpers = [
        # Class From plugins\helpers\sql_queries.py -> SqlQueries
        helpers.SqlQueries
    ]
