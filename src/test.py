import hashlib
import random
import string
from hashlib import sha256
import sys
from utils.aesutil import encrypt,decrypt 

from rich.console import Console
from rich import print as printc

from utils import dbconfig

console = Console()


db = dbconfig.dbconfig()
cursor = db.cursor()
query = "select * from pm.entries"
cursor.execute(query)

print(cursor.fetchall()[0][4])
