from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA1

import base64

key = '''-----BEGIN PUBLIC KEY-----
	MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6QdVTmGijqSVzMO3Re/KAgHh+snDvpK9BYK2XD6wRLX+ikjT0Ejb92/COWyeI0YEXLuXjLGGyBiNBDiwVe5sJ2bA8UMIeayOkEAc/xyGnzN/o105BTntAs4YeuXXno6YRDtY/A1yTiaygkD9K4Sy9L8qGVFSt+tatLl9dhp6KOAqhOsruf0YkuVMlWhhJ+zf/uQbCRvihowG8K4PLgekTPnD3t6XV87h00htyzvMuoZ8C4Iw0mh78omMv5XiQUj/E18VuLUx8cwk9qeBCs/Kuye1kr2d79UtSge/Sf4FJi2G+muWZaJBIH+uKHtQma9dETfuS2sisbW3ym8kooJThQIDAQAB
	-----END PUBLIC KEY-----
	'''

public_key = RSA.import_key(key)
# print(public_key)

msg = '4833130037628039'.encode('utf-8')

# session_key = get_random_bytes(16)
cipher_rsa = PKCS1_OAEP.new(public_key)
# cipher_rsa = PKCS1_OAEP.new(public_key, hashAlgo=SHA1)
encrypted = cipher_rsa.encrypt(msg)
print(base64.b64encode(encrypted).decode('utf-8'))