import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import create_engine, SQLModel, Session
from app.infrastructure.engine import get_session
from app.infrastructure.sqlmodels import User as sqlmodelUser
from sqlmodel.pool import StaticPool
from sqlmodel import select


TEST_DATABSE_URL = "sqlite:///:memory:"


engine = create_engine(
  TEST_DATABSE_URL,
  connect_args={"check_same_thread": False},
  poolclass=StaticPool,
  echo=True
)

@pytest.fixture
def session():
  SQLModel.metadata.create_all(engine)
  with Session(engine) as session:
    yield session

  SQLModel.metadata.drop_all(engine)

@pytest.fixture
def client(session: Session):
  app.dependency_overrides[get_session] = lambda: session
  with TestClient(app) as client:
    yield client

  app.dependency_overrides.clear()


def test_create_user_api_success(client, session):
    # pytest가 conftest.py의 client fixture를 알아서 찾아서 주입해줍니다.
    response = client.post("/users", json={
        "name": "이승욱",
        "phone_number": "01086057662",
        "password": "6940",
        "role": "사용자"
    })

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == "이승욱"
    assert "id" in data

    statement = select(sqlmodelUser).where(sqlmodelUser.phone_number == data["phone_number"])
    db_user = session.exec(statement).first()

    assert db_user is not None
    assert db_user.password != "6940"
    assert db_user.password.startswith("$argon2")



def test_create_store_api_success(client):
  response = client.post("/stores", json={
    "name": "스타벅스 경주점",
    "owner_id": 1,
    "is_5_or_more_employee": False
  })

  assert response.status_code == status.HTTP_201_CREATED
  data = response.json()
  assert data["owner_id"] == 1
  assert data["name"] == "스타벅스 경주점"