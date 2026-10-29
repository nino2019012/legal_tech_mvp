from pydantic import BaseModel
from app.domain.models import UserRole

class UserCreateRequest(BaseModel):
  name: str
  phone_number: str
  password: str
  role: UserRole

class UserResponse(BaseModel):
  id: int
  name: str
  phone_number: str
  role: UserRole

class StoreCreateRequest(BaseModel):
  name: str
  owner_id: int
  is_5_or_more_employee: bool

class StoreResponse(BaseModel):
  id: int
  name: str
  owner_id: int
  is_5_or_more_employee: bool