from sqlmodel import SQLModel, Field
from enum import Enum
from app.infrastructure.engine import engine

class UserRole(str, Enum):
  owner = "사용자"
  worker = "근로자"

class User(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  phone_number: str = Field(index=True)
  password: str
  role: UserRole

class Store(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  owner_id: int
  is_5_or_more_employee: bool

# ???
def create_db_and_tables():
  SQLModel.metadata.create_all(engine)