from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres.jnhdwwnfocyutkhidafa:$Ey+t/.#)xc62PC@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'

engine = engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

