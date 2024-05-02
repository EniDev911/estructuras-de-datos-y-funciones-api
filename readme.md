## Requerimientos

### 1. Obtener a todos los usuarios

Nos socilitan toda la información de los usuarios retornada por la API, debemos almacenarla en una variable llamada `users_data` e imprimirla en pantalla:

```python
import requests # pip install requests

endpoint = "https://reqres.in/api/users"
respuesta = requests.get(endpoint)

users_data = respuesta.json()
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