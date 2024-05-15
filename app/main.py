from fastapi import Depends, FastAPI, HTTPException

from app.model.base_model import Base
from app.database.database import engine
from app.router.item_router import item_router
from app.router.user_router import user_router



app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(item_router)





