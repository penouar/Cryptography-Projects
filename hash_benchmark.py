import hashlib
import bcrypt
from argon2 import PasswordHasher
import time

password = "mypassword123"

start = time.time()
count_sha = 0

while time.time() - start < 3:
    hashlib.sha256(password.encode()).hexdigest()
    count_sha +=1

sha_time = (time.time() - start) / count_sha

print("SHA-256")
print("Hashes in 3 seconds:", count_sha)
print("Average time per hash:", sha_time)

start = time.time()
count_bcrypt = 0

while time.time() - start < 3:
    bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    count_bcrypt += 1

bcrypt_time = (time.time() - start) / count_bcrypt

print("\nbcrypt")
print("Hashes in 3 seconds:", count_bcrypt)
print("Average time per hash:", bcrypt_time)

ph = PasswordHasher()
start = time.time()
count_argon2 = 0

while time.time() - start < 3:
    ph.hash(password)
    count_argon2 += 1

argon2_time = (time.time() - start) / count_argon2

print("\nArgon2")
print("Hashes in 3 seconds:", count_argon2)
print("Average time per hash:", argon2_time)

