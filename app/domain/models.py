from enum import Enum

class UserRole(str, Enum):
  owner = "사용자"
  worker = "근로자"

class User():

  def __init__(
      self, id: int | None, name: str, phone_number: str, password: str, role: UserRole
  ):
    self.id = id
    self.name = name
    self.phone_number = phone_number
    self.password = password
    self.role = role

class Store():

  def __init__(self, id: int | None, name: str, owner_id: int, is_5_or_more_employee: bool):
    self.id = id
    self.name = name
    self.owner_id = owner_id
    self.is_5_or_more_employee = is_5_or_more_employee