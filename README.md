# QA API Testing – Pytest + Requests

## 📌 Descripción
Proyecto de QA Automation enfocado en la validación de una API REST utilizando Pytest y Requests.  
Se realizan pruebas automatizadas sobre distintos endpoints para verificar respuestas exitosas, manejo de errores y consistencia de los datos retornados por la API.

## 🧪 Qué se está probando
- Consumo de endpoints REST
- Respuestas exitosas (GET)
- Validación de estructura y tipos de datos del JSON
- Manejo de errores y escenarios negativos (endpoint inexistente)
- Creación de recursos mediante método POST

## 🛠 Stack Tecnológico
- Python
- Pytest
- Requests
- API pública JSONPlaceholder

## 📂 Estructura del Proyecto
```
qa-api-testing/
├── tests/
│ └── test_users_get.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

- `tests/`: contiene los tests automatizados
- `pytest.ini`: configuración global de Pytest
- `requirements.txt`: dependencias del proyecto
- `.gitignore`: archivos y carpetas ignoradas por Git

## ▶️ Cómo ejecutar el proyecto
```powershell
# Clonar el repositorio e ingresar al proyecto
git clone https://github.com/Matiaslb14/qa-api-testing.git
cd qa-api-testing

# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar los tests
pytest
```

## ✅ Escenarios automatizados
- Obtención exitosa de la lista de usuarios (GET)
- Validación de estructura y tipos de datos del usuario
- Escenario negativo: respuesta 404 ante endpoint inexistente
- Creación de usuario mediante POST y validación de la respuesta

## 📝 Notas de QA
- Se validan tanto códigos de estado como el contenido de la respuesta
- Los tests están diseñados para ser simples, legibles y mantenibles
- La API utilizada simula la creación de recursos, por lo que los datos no se persisten realmente
- El proyecto está orientado a demostrar fundamentos de QA Automation aplicables a APIs reales

## 📈 Mejoras futuras
- Agregar validaciones más profundas del contrato de la API
- Separar tests por endpoint o funcionalidad
- Implementar reportes de ejecución
- Incorporar pruebas para métodos PUT y DELETE
