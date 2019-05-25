import os
import hashlib
from getpass import getpass

print('Username: ' )
passwd = getpass('Password: ')
h = hashlib.md5()
h.update(passwd.encode())
passwd_encrypt = h.hexdigest()