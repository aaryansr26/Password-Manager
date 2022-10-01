
from getpass import getpass

def computeMasterKey(mp, ds):
    password = mp.encode()
    salt = ds.encode()


def addEntry(mp, ds, sitename, siteurl, email, username):
    #get the password
    password = getpass("Password: ")
    mk = computeMasterKey(mp, ds)
    