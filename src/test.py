import hashlib
import random
import string
from hashlib import sha256
import sys
from utils.aesutil import encrypt,decrypt 

from rich.console import Console
from rich import print as printc

console = Console()


if __name__=="__main__":
    
    op = sys.argv[1]
    
    if op==1 or op=="encrypt":
        msg = sys.argv[2]
        key = sys.argv[3]
        keyType = sys.argv[4]
        cipher, newkey = encrypt(key, msg, keyType=keyType)
        print(cipher, newkey)
        
    
    elif op==2 or op == "decrypt":
        cipher = sys.argv[2]
        key = sys.argv[3]
        keyType = sys.argv[4]
        plaintext = decrypt(key, cipher, keyType=keyType)
        print(plaintext)