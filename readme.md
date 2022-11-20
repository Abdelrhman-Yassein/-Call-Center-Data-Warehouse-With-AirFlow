# Call Center Data Warehouse And ETL Project

In this project, We will Automate  transform and transfer data and build a data warehouse to make analysis easier Using Mysql Server And AirFlow
## DataSets

###  Call Center Data:
Call Center Data [this](https://data.world/markbradbourne/rwfd-real-world-fake-data/workspace/file?filename=Call+Center.csv)




## Star-Schema Model
![Star-Schema](https://raw.githubusercontent.com/Abdelrhman-Yassein/-Call-Center-Data-Warehouse-With-AirFlow/main/images/call-center.png)

## Project DAG
![Star-Schema](https://raw.githubusercontent.com/Abdelrhman-Yassein/-Call-Center-Data-Warehouse-With-AirFlow/main/images/dag.PNG)

## Data Check Result
![Star-Schema](https://raw.githubusercontent.com/Abdelrhman-Yassein/-Call-Center-Data-Warehouse-With-AirFlow/main/images/data_check.PNG)

## What We Use In Project

  01. Python.
  02. Docker 
  03. airflow
  04. jupyter notebook
  05. MySQL Server


## files and folders
#### 1 - data folder -> Contain all Data File
#### 2 - cover-and -know-data.ipynb  -> ipynb project file
#### 4 - call_center_dag.py-> Dag File  ->dags\call_center_dag.py
#### 5 - sql_queries.py -> Contain all sql queries we need to Insert Data And copy Data From CSV File ->  plugins\helpers\sql_queries.py
#### 6 - sql_queries.py -> Contain all sql queries we need to Drop And Create Tables ->  plugins\helpers\create_tables_sql.py
#### 7 - data_quality.py -> Contain My Operator to check Data ->  plugins\custom_operator\data_quality.py

## How To Run Project
    1 - You Must Update All Username and Passwrod for your Database In admin AirFlow Connection Mysql Connection
    2 - cover-and -know-data.ipynb -> Just Run Cel
    3 - Run Dag From AirFlow Ui


## Contact

## **Abdelrhman Yassein  :**  [LinkedIn](https://www.linkedin.com/in/Abdelrhman-Yassein/) - [GitHub](https://github.com/Abdelrhman-Yassein?tab=repositories)

