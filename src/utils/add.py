
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key = PBKDF2(password, salt, 32, count=10000000, hmac_hash_module=SHA512)
    return key


def addEntry(mp, ds, sitename, siteurl, email, username):
    #get the password
    password = getpass("Password: ")
    mk = computeMasterKey(mp, ds)
    
    
    