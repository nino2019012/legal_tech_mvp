from app.domain.models import User, Store
from abc import ABC, abstractmethod

# 위 가짜 db를 usecase가 받으면 결합도가 높아지니 추상 인터페이스를 선언
class UserRepositoryInterface(ABC):

  @abstractmethod
  def save(self, user: User) -> User:
    pass

  @abstractmethod
  def find_by_id(self, id: int) -> User | None:
    pass

  @abstractmethod
  def find_by_phone_number(self, phone_number: str) -> User | None:
    pass

class StoreRepositoryInterface(ABC):

  @abstractmethod
  def save(self, store: Store) -> Store:
    pass
'''
  @abstractmethod
  def find_by_owner_id(self, owner_id: int) -> Store | None:
    pass

  @abstractmethod
  def find_by_name(self, name: str) -> Store | None:
    pass
'''

class UserPasswordHasher(ABC):

  @abstractmethod
  def hash_password(self, password: str) -> str:
    pass

  @abstractmethod
  def verify_password(self, plain_password: str, hashed_password: str) -> bool:
    pass