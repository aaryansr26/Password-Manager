from rich.console import Console
import mysql.connector

console = Console()

def dbconfig():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='pm',
            passwd='password'
        )
    except Exception as e:
        console.print_exception(show_locals=True)
    
    return conn
        
        
