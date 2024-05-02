import requests # pip install requests

endpoint = "https://reqres.in/api/users"

respuesta = requests.get(endpoint)

# Obtener el listado de usuarios
print("1. Mostrando el listado de usuarios:")
users_data = respuesta.json()['data']
print(users_data)

print("---------------------------")

# Crear un usuario

print("2. Creando un nuevo usuario:")
nuevo_usuario = {
	"name": "ignacio",
	"job": "profesor"
}

respuesta = requests.post(endpoint, nuevo_usuario)
created_user = respuesta.json()
print(created_user)

print("---------------------------")

# Actualizar a un usuario
print("3. Actualizando a un usuario:")
usuario_actualizado = {
	"name": "morpheus",
	"residence": "zion"
}

respuesta = requests.put(f'{endpoint}/{users_data[1]['id']}', usuario_actualizado)
updated_user = respuesta.json()
print(updated_user)

print("---------------------------")

# Eliminar a un usuario
print("4. Mostrando el código de estado una vez eliminado el usuario: ")
for user in users_data:
    if user['first_name'] == 'Tracey':
        deleted_user = requests.delete(f'{endpoint}/{user['id']}')
        print(deleted_user.status_code)



