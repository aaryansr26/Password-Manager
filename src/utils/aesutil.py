from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import base64
from Crypto import Random
import sys

''' 
Creating functionality for AES Algorithm
Encrypt() - Encrypt function basically encrypts the given plaintext into ciphertext using a key
Decrypt() - Decrypt function basically decrypts the given ciphertext into the plaintext using the samekey
'''

def encrypt(key, source, encode=True, keyType='hex'):
    '''
    Returns base64 encoded cipher
    '''
    
    source = source.encode()
    if keyType=='hex':
        key = bytes(bytearray.fromhex(key))
    else:
        #use SHA-256 over our key to get proper-size AES key
        key = key.encode()
        key = SHA256.new(key).digest()
    
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    cipherdata = encryptor.encrypt(source)
    return base64.b64encode(cipherdata).decode() if encode else cipherdata