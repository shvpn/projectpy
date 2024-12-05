from encrypt import encrypt
from decrypt import decrypt


e=encrypt()
d=decrypt()
#SDFFMmwzbDFvMiAzSzFvMm4zMw==
message = input("Enter the message: ")
password = input("Enter the password: ")
msg = d.decrypt(message, password)

print(msg)