from app.domain.interface import StoreRepositoryInterface
from app.domain.models import Store

class CreateStoreUseCase():
  def __init__(self, repository: StoreRepositoryInterface):
    self.repo = repository

  def execute(
      self,
      name: str,
      owner_id: int,
      is_5_or_more_employee:bool,
      id: int | None = None,
    ):
    store = Store(
      id=id,
      name=name,
      owner_id=owner_id,
      is_5_or_more_employee=is_5_or_more_employee
    )
    saved_store = self.repo.save(store)

    return saved_store

class GetStoreByOwnerIdUseCase():

  def __init__(self, repository: StoreRepositoryInterface):
    self.repo = repository

  def execute(self, owner_id: int):
    store = self.repo.find_by_owner_id(owner_id)
    return store