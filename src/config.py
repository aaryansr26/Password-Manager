from getpass import getpass
import hashlib
import random
from utils.dbconfig import dbconfig
from rich import print as printc
import sys
from rich.console import Console
import string

console = Console()

def generateDeviceSecret(length = 10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))    
    

def config():
    #Create a database
    db = dbconfig()
    cursor = db.cursor()
    
    printc("[green][+] Creating new config [/green]")
    
    try:
        cursor.execute("CREATE DATABASE pm")
    except Exception as e:
        printc("[red][!] An error occured while creating database")
        console.print_exception(show_locals=True)
        sys.exit(0)
    printc("[green][+][/green] Database 'pm' created!")
    #Create table
    
    query = "CREATE TABLE pm.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'secrets' created")    
    
    #Create entries
    
    query = "CREATE TABLE pm.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"
    res = cursor.execute(query)
    printc("[green][+][/green] Table 'entries' created")
    
    
    #Create Master Password
    while 1:
        mp = getpass("Choose a MASTER PASSWORD!")
        if mp==getpass("Re-enter MASTER PASSWORD") and mp!="":
            break
        printc("[yellow][-] Please try again. [/yellow] ")
        
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of MASTER PASSWORD")
    
    
    #Generate a Device Secret
    
    ds = generateDeviceSecret()
    printc("[green][+][/green] Device Secret Generated! ")
    
    query = "INSERT INTO pm.secrets (masterkey_hash, device_secret) values (%s, %s)"
    val = (hashed_mp, ds)
    cursor.execute(query, val) 
    db.commit()
    
    printc("[green][+][/green] Added to the database! ")
    printc("[green][+] Configuration done! [/green] ")
    
    db.close()
    
config()

    
    