from logging import exception
import mysql.connector

def dbconfig():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='password'
        )
    except Exception as e:
        print(e.message)
        
        
