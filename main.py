# This is a sample Python script.
from core.password_manager_controller import create_access_key, get_access_key, \
    delete_access_key, get_access_key_by_service, set_master_key
from views import console_view


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

master_key = ""


def main():

    while True:
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("|            GESTOR DE CONTRASEÑA             |")
        console_view.show_message("+---------------------------------------------+")
        console_view.show_message("\n")

        master_key = console_view.get_user_input("Ingrese su contraseña: ")
        set_master_key(master_key)

        console_view.show_message("[1] Agregar nueva contraseña")
        console_view.show_message("[2] Ver contraseñas almacenadas")
        console_view.show_message("[3] Buscar contraseñas por servicio")
        console_view.show_message("[4] Eliminar contraseña")
        console_view.show_message("[5] Cambiar contraseña maestra")
        console_view.show_message("[6] Salir")
        console_view.show_message("\n")

        option = console_view.get_user_input("Seleccione una opción: ")

        if option == '1':
            # Create password
            create_access_key()
        elif option == '2':
            # Get password services
            get_access_key()
        elif option == '3':
            # Find password by service
            get_access_key_by_service()
        elif option == '4':
            # Delete password
            delete_access_key()
        elif option == '5':
            # Cambiar contraseña maestra
            get_access_key()
        elif option == '6':
            console_view.show_message("Saliendo de la aplicación...")
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


