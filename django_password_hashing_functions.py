
# import the hash algorithm
from passlib.hash import django_pbkdf2_sha256

"""
@author	Chandan Sharma
@link		https://github.com/devchandansh/
@since	Version 1.0.0
"""

print(django_pbkdf2_sha256.verify("123", "pbkdf2_sha256$260000$q1205pY3LBwuAqmlt1bhZx$uMu1eog5dgnTfI+YTa/dq0uxAbIC8RridPmFiqekzd0="))


"""
==================================================================
Encryption Using Library:: passlib 								
Library URL: https://passlib.readthedocs.io/en/stable/ 			
==================================================================
"""
def passlib_encryption(raw_password):
	"""
	Here, Encryption is Using passlib Library.
	"""
	# generate new salt, and hash a password
	if raw_password:
		encrypted = pbkdf2_sha256.hash(raw_password)
	else:
		encrypted = None
	
	return encrypted

#=================================================
# For Password Encryption
#=================================================
def passlib_pbkdf2_sha256_encrypt(raw_password):
	# generate new salt, and hash a password
	salt_size = 32
	rounds = 12000

	if raw_password:
		encrypted = pbkdf2_sha256.encrypt(raw_password, rounds, salt_size)
	else:
		encrypted = None
	
	return encrypted

def passlib_encryption_verify(raw_password, enc_password):
	""" 
	@returns TRUE or FALSE 
	"""
	if raw_password and enc_password:
		# verifying the password
		response = pbkdf2_sha256.verify(raw_password, enc_password)
	else:
		response = None;
	
	return response

##=================================================

