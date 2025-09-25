
# Gestor de Contraseñas en Python

Un gestor de contraseñas seguro desarrollado en **Python**, con almacenamiento cifrado en base de datos y acceso mediante una contraseña maestra.

---

## Tecnologías utilizadas
- **Python 3**
- **SQLAlchemy** (ORM para base de datos)
- **PostgreSQL** (base de datos recomendada)
- **cryptography** (cifrado AES-GCM)
- **argon2-cffi** (derivación de claves seguras con Argon2)
- **dotenv** (manejo de variables de entorno)

---

## 📂 Estructura del proyecto
```
project/
│── main.py                     # Punto de entrada
│── core/
│    └── password_manager_controller.py
│── database/
│    ├── database.py
│    ├── db_table/
│    │   └── access_key_table.py
│    └── db_query/
│        └── access_key_query.py
│── tools/
│    ├── cryptography.py
│    ├── functions.py
│    └── validations.py
│── views/
│    └── console_view.py
│── requirements.txt
```

---

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/password-manager.git
   cd password-manager
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\\Scripts\\activate      # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar la base de datos en `database/database.py`.

---

## Uso
Ejecutar el programa principal:
```bash
python main.py
```

Menú principal:
```
[1] Agregar nueva contraseña
[2] Ver contraseñas almacenadas
[3] Buscar contraseñas por servicio
[4] Eliminar contraseña
[5] Cambiar contraseña maestra
[6] Salir
```

---

## Seguridad
- Las contraseñas se almacenan usando **AES-GCM** con claves derivadas mediante **PBKDF2**.  
- Se utiliza **Argon2** para reforzar la seguridad de la clave maestra.  
- Los datos sensibles se guardan en formato **Base64** dentro de la base de datos.

---

## Autor
- Desarrollado por: *Octavio Condori Ticona*  
- Repositorio: [GitHub](https://github.com/tu-usuario/password-manager)
"""