## Requerimientos

### 1. Obtener a todos los usuarios

Nos socilitan toda la información de los usuarios retornada por la API, debemos almacenarla en una variable llamada `users_data` e imprimirla en pantalla:

```python
import requests # pip install requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']
print(users_data)
```

### 2. Crear un usuario

Crear un nuevo usuario que tenga el nombre (*name*) de **ignacio** y de trabajo (*job*) **profesor**. Guarda el diccionario de respuesta en una variable llamada created_user e imprímila en pantalla:

```python
import requests

endpoint = "https://reqres.in/api/users"

nuevo_usuario = {
	"name": "ignacio",
	"job": "profesor"
}

respuesta = requests.post(endpoint, nuevo_usuario)

created_user = respuesta.json()
print(created_user)
```

### 3. Actualizar a un usuario

Actualizar un usuario llamado **morpheus** para que tenga un campo llamado `residence` igual a **zion**. Guarde el diccionario de respuesta en una variable llamada `updated_user` e imprímila en pantalla:

```python
import requests

endpoint = "https://reqres.in/api/users/2"

usuario_actualizado = {
	"name": "morpheus",
	"residence": "zion"
}
respuesta = requests.put(endpoint, usuario_actualizado)

updated_user = respuesta.json()
print(updated_user)
```

### 4. Eliminar a un usuario

Eliminar a un usuario llamado `Tracey`. Imprima el código de respuesta en pantalla:

```python
import requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()['data']

for user in users_data:
    if user['first_name'] == 'Tracey':
        deleted_user = requests.delete(f'{endpoint}/{user['id']}')
        print(deleted_user.status_code)
```
