from app.domain.interface import UserPasswordHasher

from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

class PwdlibPasswordHaser(UserPasswordHasher):

  def hash_password(self, password: str) -> str:
    hashed_password = password_hash.hash(password)
    return hashed_password

  def verify_password(self, plain_password: str, hashed_password: str) -> bool:
    pass