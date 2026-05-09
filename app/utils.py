from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


# Password Hashing
def hash_password(password: str):
    return password_hash.hash(password)

