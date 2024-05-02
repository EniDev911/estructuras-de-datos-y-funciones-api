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