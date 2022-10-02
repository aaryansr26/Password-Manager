import utils.aesutil
from utils.dbconfig import dbconfig
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
import utils.aesutil
from rich import print as printc

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=10000000, hmac_hash_module=SHA512)
    return key


def addEntry(mp, ds, sitename, siteurl, email, username):
    #get the password
    password = getpass("Password: ")
    mk = computeMasterKey(mp, ds)
    
    encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")
    
    #add the password to Database
    db = dbconfig()
    cursor = db.cursor()
    
    query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
    val = (sitename, siteurl, email, username, encrypted)
    
    cursor.execute(query, val)
    db.commit()
    printc("[green][+][/green] Entry added in db ")
    
        