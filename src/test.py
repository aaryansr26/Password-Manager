import hashlib
import random
import string
from hashlib import sha256
import sys
from utils.aesutil import encrypt

from rich.console import Console
from rich import print as printc

console = Console()


if __name__=="__main__":
    msg = sys.argv[1]
    key = sys.argv[2]
    keyType = sys.argv[3]
    cipher = encrypt(key, msg, keyType=keyType)
    print(cipher)
