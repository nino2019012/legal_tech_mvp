from app.domain.interface import UserRepositoryInterface, UserPasswordHasher
from app.domain.models import UserRole, User

class CreateUserUseCase():
  def __init__(self, repository: UserRepositoryInterface, hasher: UserPasswordHasher):
    self.repo = repository
    self.hasher = hasher

  def execute(self, name: str, phone_number: str, password: str, role: UserRole):

    hashed_password = self.hasher.hash_password(password)
    
    user = User(
      id= None,
      name=name,
      phone_number=phone_number,
      password=hashed_password,
      role=role
    )

    saved_user = self.repo.save(user)

    return saved_user