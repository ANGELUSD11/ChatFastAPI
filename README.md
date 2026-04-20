### Agregar y activar entorno virtual

python3 -m venv .venv
source .venv/bin/activate

### Instalar dependencias
pip install -r requirements.txt

### Iniciar servidor de desarrollo
fastapi dev app.py

### Rutas
## Swagger

http:localhost:8000/api/chat/docs