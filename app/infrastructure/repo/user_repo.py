from app.domain.interface import UserRepositoryInterface
from sqlmodel import Session, select
from app.infrastructure.sqlmodels import User as SqlModelUser
from app.domain.models import User as DomainUser

class SqlmodelUserRepository(UserRepositoryInterface):

  def __init__(self, session: Session):
    self.session = session

  def save(self, domain_user: DomainUser):
    db_user = SqlModelUser(
      id=domain_user.id,
      name=domain_user.name,
      phone_number=domain_user.phone_number,
      password=domain_user.password,
      role=domain_user.role
    )
    self.session.add(db_user)
    self.session.commit()
    self.session.refresh(db_user)

    # 매개변수로 받은 domain_user는 id가 없다!
    return DomainUser(
      id=db_user.id,
      name=db_user.name,
      phone_number=db_user.phone_number,
      password=db_user.password,
      role=db_user.role
    )

  def find_by_id(self, id: int):
    db_user = self.session.get(SqlModelUser, id)

    if not db_user:
      return None
    
    return DomainUser(
      id=db_user.id,
      name=db_user.name,
      phone_number=db_user.phone_number,
      password=db_user.password,
      role=db_user.role
    )

  def find_by_phone_number(self, phone_number: str):
    # session.get은 primary key일때만 사용
    statement = select(SqlModelUser).where(SqlModelUser.phone_number == phone_number)
    db_user = self.session.exec(statement).first()

    if not db_user:
      return None
    
    return DomainUser(
      id=db_user.id,
      name=db_user.name,
      phone_number=db_user.phone_number,
      password=db_user.password,
      role=db_user.role
    )

  