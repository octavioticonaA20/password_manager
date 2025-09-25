from contextlib import contextmanager
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

load_dotenv()

db_user = str(os.getenv("DB_USER"))
db_password = str(os.getenv("DB_PASS"))
db_host = str(os.getenv("DB_HOST"))
db_port = str(os.getenv("DB_PORT"))
db_database = str(os.getenv("DB_DATABASE"))

database_config = "postgresql://" + db_user + ":" + db_password + "@" + db_host + ":" + db_port + "/" + db_database

print(database_config)
engine = create_engine(database_config)

Base = declarative_base()


@contextmanager
def db_session_manager():
    with Session(engine, expire_on_commit=False) as db:
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise


def db_insert_table(db, item):
    try:
        db.add(item)
        db.flush()
        return item
    except Exception as e:
        raise e