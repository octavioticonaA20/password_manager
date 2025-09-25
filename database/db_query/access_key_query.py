import datetime

from database.db_table.access_key_table import AccessKeyDB


def db_get_access_key_by_service(db, service_name:str):
    try:
        return db.query(AccessKeyDB).filter(AccessKeyDB.servicio ==service_name,AccessKeyDB.activo).first()

    except Exception as e:
        print("Exception: "+ str(e))
        raise e


def db_get_all_access_key(db):
    try:
        return db.query(AccessKeyDB).filter(AccessKeyDB.activo).all()

    except Exception as e:
        print("Exception: "+ str(e))
        raise e


def db_delete_access_key(db, service_name:str):
    try:
        now = datetime.datetime.now()
        delete_row = (db.query(AccessKeyDB)
        .filter(AccessKeyDB.servicio == service_name)
        .update(
            {
                "activo": False,
                "actualizado": now
            }
        ))
        return delete_row

    except Exception as e:
        print("Exception: "+ str(e))
        raise e