from fastapi import FastAPI, Depends, status
from app.api.schema import UserResponse, UserCreateRequest, StoreCreateRequest, StoreResponse
from app.api.deps import get_create_user_case, get_create_store_case
from typing import Annotated
from app.usecase.create_user import CreateUserUseCase
from app.usecase.create_store import CreateStoreUseCase
from app.infrastructure.sqlmodels import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_tables()
  yield

app = FastAPI(lifespan=lifespan)

@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
  request: UserCreateRequest,
  user_case: Annotated[CreateUserUseCase, Depends(get_create_user_case)]
):
  created_user = user_case.execute(
    name=request.name,
    phone_number=request.phone_number,
    password=request.password,
    role=request.role
  )
  return created_user

@app.post("/stores", response_model=StoreResponse, status_code=status.HTTP_201_CREATED)
def create_store(
  request: StoreCreateRequest,
  store_case: Annotated[CreateStoreUseCase, Depends(get_create_store_case)]
):
  created_store = store_case.execute(
    name=request.name,
    owner_id=request.owner_id,
    is_5_or_more_employee=request.is_5_or_more_employee
  )
  return created_store