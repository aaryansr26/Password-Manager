
from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()
    key =


def addEntry(mp, ds, sitename, siteurl, email, username):
    #get the password
    password = getpass("Password: ")
    mk = computeMasterKey(mp, ds)
    
    