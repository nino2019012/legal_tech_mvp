from app.domain.interface import StoreRepositoryInterface
from sqlmodel import Session
from app.domain.models import Store as DomainStore
from app.infrastructure.sqlmodels import Store as SqlmodelStore

class SqlmodelStoreRepository(StoreRepositoryInterface):

  def __init__(self, session: Session):
    self.session = session

  def to_domain(self, store: SqlmodelStore) -> DomainStore:
      return DomainStore(
            id=store.id,
            name=store.name,
            owner_id=store.owner_id,
            is_5_or_more_employee=store.is_5_or_more_employee
          )

  def save(self, store: DomainStore) -> DomainStore:
    sqlmodel_store = SqlmodelStore(
      id=store.id,
      name=store.name,
      owner_id=store.owner_id,
      is_5_or_more_employee=store.is_5_or_more_employee
    )

    self.session.add(sqlmodel_store)
    self.session.commit()
    self.session.refresh(sqlmodel_store)

    return self.to_domain(sqlmodel_store)