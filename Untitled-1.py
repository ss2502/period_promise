pip install pandas
pip install mysql.connector
import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Function to create database connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Define your database connection parameters
host = '127.0.0.1'
database = 'period_promise'
user = 'root'
password = 'Topper@90'

# Create a database connection
connection = create_connection(host, user, password, database)