from app.infrastructure.repo.user_repo import SqlmodelUserRepository
from app.infrastructure.repo.sql_store_repo import SqlmodelStoreRepository
from app.usecase.create_user import CreateUserUseCase
from app.usecase.create_store import CreateStoreUseCase
from app.infrastructure.engine import SessionDep
from app.infrastructure.security import PwdlibPasswordHaser

def get_create_user_case(session: SessionDep) -> CreateUserUseCase:
  sqlmodel_repo = SqlmodelUserRepository(session)
  pwdlib_hasher = PwdlibPasswordHaser()
  return CreateUserUseCase(repository=sqlmodel_repo, hasher=pwdlib_hasher)

def get_create_store_case(session: SessionDep) -> CreateStoreUseCase:
  sqlmodel_repo = SqlmodelStoreRepository(session)
  return CreateStoreUseCase(repository=sqlmodel_repo)