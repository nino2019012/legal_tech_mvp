import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from test.fake_db.fakes import FakeStoreRepository, FakeUserRepository, FakePasswordHasher
from app.usecase.create_store import CreateStoreUseCase, GetStoreByOwnerIdUseCase
from app.usecase.create_user import CreateUserUseCase
from app.domain.models import UserRole, User

def test_create_user_success():
  fake_repo = FakeUserRepository()
  fake_hasher = FakePasswordHasher()
  usecase = CreateUserUseCase(repository=fake_repo, hasher=fake_hasher)

  created_user = usecase.execute(
    name="이승욱",
    phone_number="01086057662",
    password="6940",
    role=UserRole.owner
  )

  assert created_user.id == 1
  assert created_user.role == UserRole.owner

def test_create_hash_password():
  fake_repo = FakeUserRepository()
  fake_hasher = FakePasswordHasher()
  usecase= CreateUserUseCase(repository= fake_repo, hasher= fake_hasher)

  hashed_user = usecase.execute(
    name="이승욱",
    phone_number="01086057662",
    password="6940",
    role=UserRole.owner
  )

  assert hashed_user.password == "hashed_6940"

def test_verify_hash_password():
  fake_repo = FakeUserRepository()
  fake_hasher = FakePasswordHasher()

  create_user_usecase= CreateUserUseCase(repository= fake_repo, hasher= fake_hasher)
  create_user_usecase.execute(
    name="이승욱",
    phone_number="01086057662",
    password="6940",
    role=UserRole.owner
  )

  usecase = VerifyPasswordUseCase(respository=fake_repo, hasher=fake_hasher)

  is_valid = usecase.execute(phone_number="01086057662", plain_password="6940")

  assert is_valid is True



def test_create_store_success():
  fake_repo = FakeStoreRepository()
  usecase = CreateStoreUseCase(repository=fake_repo)

  created_store =usecase.execute(
    id=None,
    name="스타벅스 경주점",
    owner_id=1,
    is_5_or_more_employee=False
  )

  assert created_store.id == 1
  assert created_store.name == "스타벅스 경주점"
  assert created_store.owner_id == 1
  assert created_store.is_5_or_more_employee == False
  assert len(fake_repo.stores) == 1

def test_get_store_by_owner_id():
  fake_repo = FakeStoreRepository()
  usecase = CreateStoreUseCase(repository=fake_repo)

  created_store = usecase.execute(
    id=None,
    name="스타벅스 경주점",
    owner_id=10,
    is_5_or_more_employee=False
  )

  assert created_store.id is not None

  usecase1 = GetStoreByOwnerIdUseCase(repository=fake_repo)
  db_store = usecase1.execute(owner_id=10)

  assert db_store is not None
  assert db_store.owner_id == created_store.owner_id
  assert db_store.name == "스타벅스 경주점"





if __name__ == "__main__":
  test_create_user_success()
  #test_create_store_success()