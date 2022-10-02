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
    # else:
    #     #use SHA-256 over our key to get proper-size AES key
    #     key = key.encode()
    #     key = SHA256.new(key).digest()
    
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    cipherdata = IV + encryptor.encrypt(source)
    return base64.b64encode(cipherdata).decode() if encode else cipherdata


def decrypt(key, source, decode=True,keyType="hex"):
	'''
	Parameters:
	key - key to decrypt with. It can either be an ascii string or a string in hex representation. Default is hex representation
	source - the cipher (or encrypted message) to decrypt
	decode - whether to first base64 decode the cipher before trying to decrypt with the key. Default is true
	keyType - specify the type of key passed
	Returns:
	The decrypted data
	'''

	source = source.encode()
	if decode:
		source = base64.b64decode(source)

	if keyType == "hex":
		# Convert key to bytes
		key = bytes(bytearray.fromhex(key))
	# else:
	# 	# use SHA-256 over our key to get a proper-sized AES key
	# 	key = key.encode()
	# 	key = SHA256.new(key).digest()  

	IV = source[:AES.block_size]  # extract the IV from the beginning
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source[AES.block_size:])  # decrypt
	padding = data[-1]  
	if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
		raise ValueError("Invalid padding...")
	return data[:-padding]  # remove the padding
