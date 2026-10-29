from app.domain.models import User, Store
from app.domain.interface import UserRepositoryInterface ,StoreRepositoryInterface, UserPasswordHasher

# 가짜 db
class FakeUserRepository(UserRepositoryInterface):

  def __init__(self):
    self.users = []

  def save(self, user: User) -> User:
    if user.id is None:
      user.id = len(self.users) + 1
    self.users.append(user)

    return user

  def find_by_id(self, id: int) -> User | None:
    if id is None:
      raise ValueError("id가 없습니다.")
    for user in self.users:
      if user.id == id:
        return user

    return None

  def find_by_phone_number(self, phone_number):
    if phone_number is None:
      raise ValueError("phone_number가 없습니다.")
    for user in self.users:
      if user.phone_number == phone_number:
        return user
    return None

class FakePasswordHasher(UserPasswordHasher):

  def hash_password(self, password: str) -> str:
    # 암호화로 접두어 붙이기
    return f"hashed_{password}"

  def verify_password(self, plain_password: str, hashed_password:str) -> bool:
    return f"hashed_{plain_password}" == hashed_password


# 가게 저장 db
class FakeStoreRepository(StoreRepositoryInterface):

  def __init__(self):
    self.stores: list[Store] = []

  def save(self, store: Store) -> Store:
    # 데이터베이스에서 id를 생성
    if store.id is not None:
      raise ValueError("신규 생성은 id를 가질 수 없습니다.")
    store.id = len(self.stores) + 1
    self.stores.append(store)

    return store

  def find_by_owner_id(self, owner_id: int) -> Store | None:
    if owner_id is None:
      raise ValueError("id가 없습니다.")
    for store in self.stores:
      if store.owner_id == owner_id:
        return store
    return None

  def find_by_name(self, name: str) -> Store | None:
    if name is None:
      raise ValueError("가게 이름이 없습니다.")
    for store in self.stores:
      if store.name == name:
        return store
    return None

  