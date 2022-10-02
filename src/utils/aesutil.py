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