from app.database.database import get_db
from app.schema.item import Item, ItemCreate
from app.controller import item_controller
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

item_router = APIRouter(tags=['Item'])

@item_router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return item_controller.create_user_item(db=db, item=item, user_id=user_id)


@item_router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item_controller.get_items(db, skip=skip, limit=limit)
    return items