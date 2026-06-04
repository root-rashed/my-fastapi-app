from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


# Password Hashing
def hash_password(password: str):
    return password_hash.hash(password)


def verify_password(plain,hashed):
    return password_hash_verify(plain,hashed)