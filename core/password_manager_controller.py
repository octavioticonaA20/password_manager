import datetime

from database.database import db_session_manager, db_insert_table
from database.db_query.access_key_query import db_get_all_access_key, db_get_access_key_by_service, db_delete_access_key
from database.db_table.access_key_table import AccessKeyDB

from tools.cryptography import generate_derived_master_key, encrypt_AES, decrypt_AES
from tools.functions import bytes_a_base64, base64_a_bytes
from tools.validations import equal_password_validation
from views import console_view


master_key = ""


def set_master_key(_master_key: str):
    global master_key
    master_key = _master_key


def get_access_key_by_service():
    with db_session_manager() as db:
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("|       BUSCAR CONTRASEÑA POR SERVICIO        |")
        console_view.show_message("+---------------------------------------------+")

        service_name = console_view.get_user_input("Ingrese el nombre del servicio: ")

        result_db =db_get_access_key_by_service(db, service_name)

        if result_db:
            console_view.show_message("#\tServicio\tUsuario \tFecha")
            console_view.show_message("-----------------------------------------------")

            console_view.show_message(f"1\t{result_db.servicio}\t{result_db.usuario} \t{result_db.creado.strftime("%Y-%m-%d")}")

            option = console_view.get_user_input("Seleccione un número para ver detalles o '0' para volver")

            if option == '0':
                return None
            else:
                option = console_view.get_user_input("Seleccione un número para ver detalles o '0' para volver")
        else:
            console_view.show_message("No se tiene registros para la busqueda.")
            console_view.show_message("\n")
            option = console_view.get_user_input("'1' intentar nuevamente o '0' para volver")

            if option == '0':
                return None
            else:
                get_access_key_by_service()


def get_access_key():
    with db_session_manager() as db:
        result_db = db_get_all_access_key(db)
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("|          CONTRASEÑAS ALMACENADAS            |")
        console_view.show_message("+---------------------------------------------+")

        if result_db:
            console_view.show_message("#\tServicio\tUsuario \tFecha")
            console_view.show_message("-----------------------------------------------")
            item_number = 0
            for item in result_db:
                item_number+=1
                console_view.show_message(f"{item_number}\t{item.servicio}\t{item.usuario} \t{item.creado.strftime("%Y-%m-%d")}")

            option = console_view.get_user_input("Seleccione un número para ver detalles o '0' para volver: ")

            if option == '0':
                return None
            else:
                get_detail_access_key(int(option), result_db)
                # option = console_view.get_user_input("Seleccione un número para ver detalles o '0' para volver")

            # return AccessKeyModel(
            #     id=result_db.id,
            #     service_name=result_db.servicio,
            #     user=result_db.usuario,
            #     date_create=result_db.creado
            # )
        else:
            console_view.show_message("No se tiene registros para la busqueda.")
            console_view.show_message("\n")
            return None


def create_access_key():
    try:
        with db_session_manager() as db:
            console_view.show_message("+---------------------------------------------+")
            console_view.show_message("|          AGREGAR NUEVA CONTRASEÑA           |")
            console_view.show_message("+---------------------------------------------+")
            service_name = console_view.get_user_input("Ingrese el nombre del servicio: ")
            user_service = console_view.get_user_input("Ingrese el usuario o correo: ")

            equal_password = False
            for i in range(3):
                password_service = console_view.get_user_input("Ingrese la contraseña: ")
                confirm_password_service = console_view.get_user_input("Confirmar contraseña: ")

                if equal_password_validation(password_service, confirm_password_service):
                    equal_password = True
                    break
                else:
                    console_view.show_message("ERROR: Las contraseñas no coinciden, intente nuevamente.")

            if not equal_password:
                console_view.show_message("Cantidad de intentos superado, vuela a intentarlo.")
                # retornar a pantalla principal

            now = datetime.datetime.now()
            derived_key, salt = generate_derived_master_key(master_key)

            password_service_bytes = password_service.encode()
            encrypt_password, tag, iv = encrypt_AES(derived_key, password_service_bytes)

            # Almacenamiento de la contraseña
            create_access_key_db = AccessKeyDB(
                id=None,
                servicio=service_name,
                usuario=user_service,
                password_encriptado=bytes_a_base64(encrypt_password),
                salt=bytes_a_base64(salt),
                iv=bytes_a_base64(iv),
                tag=bytes_a_base64(tag),
                activo=True,
                creado=now,
                actualizado=now
            )

            result_create = db_insert_table(db, create_access_key_db)

            if result_create:
                console_view.show_message("Contraseña creada exitosamente.")
                option = console_view.get_user_input("Seleccione '0' para volver")

                if option == '0':
                    return None
            else:
                console_view.show_message("Error la contraseña no pudo crearse.")
                option = console_view.get_user_input("Seleccione '1' intentar nuevamente o '0' para volver")

                if option == '0':
                    return None
                else:
                    create_access_key()

            return result_create

    except Exception as e:
        raise e


def delete_access_key():
    with db_session_manager() as db:
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("|       ELIMINAR CONTRASEÑA ALMACENADAS       |")
        console_view.show_message("+---------------------------------------------+")

        result_db = db_get_all_access_key(db)
        if result_db:
            console_view.show_message("#\tServicio\tUsuario \tFecha")
            console_view.show_message("-----------------------------------------------")
            item_number = 0
            for item in result_db:
                item_number+=1
                console_view.show_message(f"{item_number}\t{item.servicio}\t{item.usuario} \t{item.creado.strftime("%Y-%m-%d")}")

            service_name = console_view.get_user_input("Insert el nombre del servicio a eliminar: ")

            row_delete = db_delete_access_key(db, service_name)

            if row_delete:
                console_view.show_message("Registro eliminado exitosamente")
                option = console_view.get_user_input("Seleccione '0' para volver")

                if option == '0':
                    return None

        else:
            console_view.show_message("No se tienen servicios para eliminar")
            option = console_view.get_user_input("Seleccione '0' para volver")

            if option == '0':
                return None


def get_detail_access_key(option: int, db_result):
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("|            DETALLE DE CONTRASEÑA            |")
        console_view.show_message("+---------------------------------------------+")
        iterador=0
        for item in db_result:
            iterador += 1
            if iterador == option:
                console_view.show_message("#\tServicio \tUsuario \tContraseña decriptada \tFecha creación \tFecha actualización")
                console_view.show_message("------------------------------------------------------------------------------------------------------------")
                pass_plain = decrypted_password(master_key, base64_a_bytes(item.salt), base64_a_bytes(item.password_encriptado), base64_a_bytes(item.iv), base64_a_bytes(item.tag))
                console_view.show_message(
                        f"{iterador}\t{item.servicio}\t{item.usuario}\t{pass_plain} \t{item.creado.strftime("%Y-%m-%d")} \t{item.actualizado.strftime("%Y-%m-%d")}")

                option = console_view.get_user_input("Seleccione '0' para volver: ")
                break

        return None


def decrypted_password(master_key,salt, pass_encrypted, iv, tag):
    derived_key, _ = generate_derived_master_key(master_key, salt)

    return decrypt_AES(derived_key, pass_encrypted, iv, tag)