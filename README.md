# QA API Testing – Pytest + Requests

## 📌 Descripción
Proyecto de **QA Automation** enfocado en la validación de una **API REST** utilizando **Pytest** y **Requests**.  
El objetivo es automatizar pruebas sobre distintos endpoints para verificar respuestas exitosas, manejo de errores y consistencia de los datos retornados por la API, aplicando fundamentos de testing de APIs utilizados en escenarios reales.

Se utiliza una **API pública (JSONPlaceholder)** para simular un entorno de pruebas sin dependencias externas.

## ⭐ Características / Features Clave
- Automatización de pruebas de **APIs REST** con **Pytest**
- Validación de códigos de estado **HTTP**
- Validación de estructura y tipos de datos del **JSON**
- Manejo de escenarios positivos y negativos
- Pruebas de creación de recursos mediante método **POST**
- Proyecto orientado a **fundamentos de QA Automation** en APIs

## 🧪 Qué se está probando
- Consumo de endpoints REST
- Respuestas exitosas (`GET`)
- Validación de estructura y tipos de datos del **JSON**
- Manejo de errores ante endpoints inexistentes (`404`)
- Creación de recursos mediante método `POST`

## 🛠 Stack Tecnológico
- **Python**
- **Pytest**
- **Requests**
- API pública JSONPlaceholder

## 📂 Estructura del Proyecto
```text
qa-api-testing/
├── tests/
│  └── test_users_get.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```
## ▶️ Cómo ejecutar el proyecto
``` powershell
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
- Obtención exitosa de la lista de usuarios (`GET`)
- Validación de estructura y tipos de datos del usuario
- Respuesta `404` ante endpoint inexistente
- Creación de usuario mediante `POST` y validación de la respuesta

## 🧠 Decisiones técnicas
- Se utiliza **JSONPlaceholder** como API pública para simular un entorno real de pruebas.
- Se validan tanto códigos de estado **HTTP** como el contenido de las respuestas.
- Los tests están diseñados para ser simples, legibles y fáciles de mantener.
- La API simula la creación de recursos, por lo que los datos no se persisten realmente, comportamiento documentado como parte del testing.

## 📊 Reportes / Evidencia (cuando aplique)
- La ejecución de los tests se valida mediante la salida estándar de **Pytest**.
- No se incluyen evidencias visuales al tratarse de un proyecto de **fundamentos de testing de APIs**.

## 📈 Mejoras futuras
- Agregar validaciones más profundas del contrato de la API
- Separar tests por endpoint o funcionalidad
- Implementar reportes de ejecución
- Incorporar pruebas para métodos `PUT` y `DELETE`