from fastapi import APIRouter, Depends
import schemas, models
from sqlalchemy.orm  import Session
from cruds import crud
from config.db import SessionLocal, engine

user = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@user.get("/")

def bienvenida():
    return "Hola 9b"

@user.get("/users", response_model=list[schemas.users],tags=["Usuarios"])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# @user.get("/user", response_model=List[model_user], tags=["Usuarios"])
# def get_users(id: Optional[str] = Query(None, description="ID del usuario a buscar")):
#     if id:
#         filtered_users = [user for user in users if user.id == id]
#         if not filtered_users:
#             raise HTTPException(status_code=404, detail="User not found")
#         return filtered_users
#     return users


# # Método POST
# @user.post("/users", response_model=model_user, tags=["Usuarios"])
# def save_users(insert_users: model_user):
#     users.append(insert_users)
#     print(insert_users)
#     return insert_users

# # Método PUT
# @user.put("/edit_user", response_model=model_user, tags=["Usuarios"])
# def update_user(user_id: str, updated_user: model_user):
#     for index, user in enumerate(users):
#         if user.id == user_id:
#             users[index] = updated_user
#             return updated_user
#     raise HTTPException(status_code=404, detail="User not found")

# # Método DELETE
# @user.delete("/delete_user", tags=["Usuarios"])
# def delete_user(user_id: str):
#     for index, user in enumerate(users):
#         if user.id == user_id:
#             del users[index]
#             return {"detail": "User deleted"}
#     raise HTTPException(status_code=404, detail="User not found")
